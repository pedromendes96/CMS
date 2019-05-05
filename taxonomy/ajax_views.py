from utils.views import AjaxView
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
from django.contrib.admin.utils import quote
from .models import Section, Category
from .admin import TaxonomyModelAdmin, SectionModelAdmin, CategoryModelAdmin

import logging
logger = logging.getLogger("taxonomy")

CLASSES = {
    Section.__name__: Section,
    Category.__name__: Category
}


class AjaxTreeStructure(AjaxView):
    def get(self, request, *args, **kwargs):
        all_data = []
        sections = Section.get_sections()
        model_admin = SectionModelAdmin()
        for section in sections:
            section_data = dict()
            section_data["id"] = Section.__name__ + "_" + str(section.pk)
            section_data["text"] = str(section)
            section_data["type"] = str(section.active).lower()
            section_data["li_attr"] = {
                "data-status": section.active,
                "data-edit": reverse(model_admin.url_helper.get_action_url_name('edit'), kwargs={
                    "instance_pk": section.pk
                }),
                "class": section.active
            }
            section_data["children"] = self._get_categories_hierarchy(section)
            all_data.append(section_data)
        logger.info("output: {}".format(all_data))
        return JsonResponse(data=all_data, safe=False)

    def _get_categories_hierarchy(self, section):
        all_data_categories = []
        main_categories = section.get_main_categories()
        for category in main_categories:
            category_context = self._recursive_category(category)
            all_data_categories.append(category_context)
        return all_data_categories

    def _recursive_category(self, category):
        context = dict()
        model_admin = CategoryModelAdmin()
        context["id"] = Category.__name__ + "_" + str(category.pk)
        context["text"] = str(category)
        context["type"] = str(category.active).lower()
        context["li_attr"] = {
            "data-status": category.active,
            "data-edit": reverse(model_admin.url_helper.get_action_url_name('edit'), kwargs={
                "instance_pk": category.pk
            }),
            "class": category.active
        }
        children_data = []
        children = category.get_children()
        if children.count() == 0:
            return context
        else:
            for child in children:
                children_data.append(self._recursive_category(child))
        context["children"] = children_data
        return context


class OnMove(AjaxView):
    def post(self, request, *args, **kwargs):
        class_name = request.POST.get("class")
        identifier = request.POST.get("id")
        sort_order = request.POST.get("position")

        chosen_class = CLASSES.get(class_name)
        instance = chosen_class.objects.get(pk=identifier)

        if request.POST.get("has_parent") == "true":
            parent_class_name = request.POST.get("parent_class")
            parent_identifier = request.POST.get("parent_id")

            parent_chosen_class = CLASSES.get(parent_class_name)
            parent_instance = parent_chosen_class.objects.get(
                pk=parent_identifier)

            if isinstance(parent_instance, Section):
                if isinstance(instance, Section):

                    category = Category(
                        name=instance.name, section=parent_instance, parent=None, sort_order=sort_order)
                    category.save()

                    Category.objects.filter(section=instance).update(
                        section=None, parent=category)

                    instance.delete()
                else:
                    instance.section = parent_instance
                    instance.parent = None
                    instance.sort_order = sort_order
                    instance.save()
            else:
                if isinstance(instance, Section):
                    category = Category(
                        name=instance.name, section=None, parent=parent_instance, sort_order=sort_order)
                    category.save()
                    instance.delete()
                else:
                    instance.section = None
                    instance.parent = parent_instance
                    instance.save()
        else:
            if isinstance(instance, Section):
                # only change order
                instance.sort_order = sort_order
                instance.save(update_fields=["sort_order"])
            else:
                section = Section.objects.create(
                    name=instance.name, sort_order=sort_order)
                instance.get_children().update(parent=None, section=section)
                instance.delete()
        return JsonResponse({
            "result": "OK",
            "id": type(instance).__name__ + "_" + str(instance.pk),
        })


class OnInactivate(AjaxView):
    def post(self, request, *args, **kwargs):
        class_name = request.POST.get("class")
        identifier = request.POST.get("id")

        chosen_class = CLASSES.get(class_name)
        instance = chosen_class.objects.get(pk=identifier)
        instance.set_inactive()
        logger.info("Now instance {} have active:{}".format(
            instance, instance.active))
        return JsonResponse({
            "result": "OK",
            "id": type(instance).__name__ + "_" + str(instance.pk),
            "active": instance.active
        })


class OnActivate(AjaxView):
    def post(self, request, *args, **kwargs):
        class_name = request.POST.get("class")
        identifier = request.POST.get("id")

        chosen_class = CLASSES.get(class_name)
        instance = chosen_class.objects.get(pk=identifier)
        instance.set_active()
        logger.info("Now instance {} have active:{}".format(
            instance, instance.active))
        return JsonResponse({
            "result": "OK",
            "id": type(instance).__name__ + "_" + str(instance.pk),
            "active": instance.active
        })


class OnCreate(AjaxView):
    def post(self, request, *args, **kwargs):
        class_name = request.POST.get("class")

        parent_class_name = request.POST.get("parent_class")
        parent_identifier = request.POST.get("parent_id")

        chosen_class = CLASSES.get(class_name)
        instance = chosen_class(name=request.POST.get("name"))
        instance.save()

        parent_chosen_class = CLASSES.get(parent_class_name)
        parent_instance = parent_chosen_class.objects.get(pk=parent_identifier)

        if isinstance(parent_instance, Section):
            parent_instance.add_category(instance)
        else:
            parent_instance.add_child(instance)

        return JsonResponse({
            "result": "OK",
            "id": type(instance).__name__ + "_" + str(instance.pk),
        })


class OnRename(AjaxView):
    def post(self, request, *args, **kwargs):
        class_name = request.POST.get("class")
        identifier = request.POST.get("id")

        chosen_class = CLASSES.get(class_name)

        instance = chosen_class.objects.get(pk=identifier)
        instance.name = request.POST.get("name")
        instance.save()

        return JsonResponse({
            "result": "OK",
            "id": type(instance).__name__ + "_" + str(instance.pk),
        })

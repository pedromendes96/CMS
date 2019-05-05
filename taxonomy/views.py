from django.shortcuts import render
from wagtail.contrib.modeladmin.views import IndexView
from .models import Section, Category
# Create your views here.


class SectionIndexView(IndexView):
    def get_context_data(self, **kwargs):
        sections = self.get_base_queryset()
        all_data = []
        for section in sections:
            section_data = dict()
            section_data["instance"] = section
            section_data["children"] = self._get_categories_hierarchy(section)
            all_data.append(section_data)

        context = {
            "data": all_data,
            "category_name": Category.__name__,
            "section_name": Section.__name__
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def _get_categories_hierarchy(self, section):
        all_data_categories = []
        main_categories = section.get_main_categories()
        for category in main_categories:
            category_context = self._recursive_category(category)
            all_data_categories.append(category_context)
        return all_data_categories

    def _recursive_category(self, category):
        context = dict()
        context["instance"] = category
        children_data = []
        children = category.get_children()
        if children.count() == 0:
            return context
        else:
            for child in children:
                children_data.append(self._recursive_category(child))
        context["children"] = children_data
        return context

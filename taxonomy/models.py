from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

from simple_history.models import HistoricalRecords

from utils.models import ActivatableOrderableModel, ActivatableModel
from wagtail.admin.edit_handlers import FieldPanel

import logging

User = get_user_model()

logger = logging.getLogger("taxonomy")
# Create your models here.


class SectionTag(TaggedItemBase):
    content_object = ParentalKey(
        'Section',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class Section(ClusterableModel, ActivatableOrderableModel):
    name = models.CharField(verbose_name=_(
        "Name"), max_length=32, null=False, blank=False)
    # tags = TaggableManager(blank=True)
    hex_color = models.CharField(verbose_name=_(
        "Hex Color"), null=False, blank=False, max_length=16)
    users = models.ManyToManyField(User, through="UsersFollowingSection")
    history = HistoricalRecords()
    tags = ClusterTaggableManager(through=SectionTag, blank=True)
    # tags = TaggableManager(blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('hex_color'),
        FieldPanel('tags'),
    ]

    def __str__(self):
        return "{}".format(self.name)

    def get_categories_hierarchy(self):
        all_data_categories = []
        main_categories = self.get_main_categories()
        for category in main_categories:
            category_context = category.recursive_category()
            all_data_categories.append(category_context)
        return all_data_categories

    def add_category(self, category):
        category.section = self
        category.save(update_fields=["section"])

    def follow(self, user):
        users_following_sections = UsersFollowingSection.objects.filter(
            user=user, section=self)
        if users_following_sections.count() == 0:
            instance = UsersFollowingSection.objects.create(
                user=user, section=self)
        else:
            instance = users_following_sections.first()
            instance.active = True
            instance.save(update_fields=["active"])

    def unfollow(self, user):
        users_following_sections = UsersFollowingSection.objects.filter(
            user=user, section=self)
        if users_following_sections.count() > 0:
            instance = users_following_sections.first()
            instance.active = False
            instance.save(update_fields=["active"])

    def get_main_categories(self):
        return Category.objects.filter(parent=None, section=self).order_by("sort_order")

    def get_active_main_categories(self):
        return Category.objects.filter(parent=None, active=True, section=self).order_by("sort_order")

    @staticmethod
    def get_sections():
        return Section.objects.all().order_by("sort_order")

    @staticmethod
    def get_active_sections():
        return Section.objects.filter(active=True).order_by("sort_order")

    def on_activation(self):
        categories = Category.objects.filter(section=self)
        for category in categories:
            category.active = True
            category.save(update_fields=["active"])

    def on_desactivation(self):
        categories = Category.objects.filter(section=self)
        for category in categories:
            category.active = False
            category.save(update_fields=["active"])


class UsersFollowingSection(ActivatableModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)


class CategoryTag(TaggedItemBase):
    content_object = ParentalKey(
        'Category',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class AbstractCategory(ClusterableModel, ActivatableOrderableModel):
    name = models.CharField(verbose_name=_(
        "Name"), max_length=32, null=False, blank=False)
    tags = ClusterTaggableManager(through=CategoryTag, blank=True)

    class Meta:
        abstract = True


class Category(AbstractCategory):
    img = models.ImageField(verbose_name=_("Image"), null=True, blank=True)
    description = models.CharField(verbose_name=_(
        "Description"), max_length=32, null=False, blank=False)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(
        Section, null=True, blank=True, on_delete=models.CASCADE, related_query_name="section")
    history = HistoricalRecords()

    panels = [
        FieldPanel('name'),
        FieldPanel('img'),
        FieldPanel('description'),
        FieldPanel('tags'),
    ]

    def __str__(self):
        return "{}".format(self.name)

    def recursive_category(self):
        context = dict()
        context["instance"] = self
        children_data = []
        children = self.get_children()
        if children.count() == 0:
            return context
        else:
            for child in children:
                children_data.append(child.recursive_category())
        context["children"] = children_data
        return context

    def get_active_children(self):
        return Category.objects.filter(parent=self, active=True).order_by("sort_order")

    def get_children(self):
        return Category.objects.filter(parent=self).order_by("sort_order")

    @staticmethod
    def get_active_main_categories():
        return Category.objects.filter(parent=None, active=True).order_by("sort_order")

    def add_child(self, category):
        category.parent = self
        category.save(update_fields=["parent"])

    def on_activation(self):
        self.recursive_enable()

    def on_desactivation(self):
        self.recursive_disable()

    def recursive_disable(self):
        categories = Category.objects.filter(parent=self)
        for category in categories:
            category.active = False
            category.save()
            category.recursive_disable()

    def recursive_enable(self):
        categories = Category.objects.filter(parent=self)
        for category in categories:
            category.active = True
            category.save()
            category.recursive_enable()

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from wagtail.core.models import Orderable

import json


# Create your models here.
class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save(update_fields=kwargs.keys())

    @classmethod
    def create_or_update(cls, filter_context, update_data_context=None):
        created = False
        create_data_context = filter_context.copy()
        if update_data_context:
            create_data_context.update(update_data_context)

        queryset = cls.objects.filter(**filter_context)
        if queryset.count() > 0:
            if update_data_context:
                instance = cls.objects.get(**filter_context)
                instance.update(**update_data_context)
            else:
                instance = queryset.first()
        else:
            instance = cls.objects.create(
                **create_data_context)
            created = True
        return (instance, created)

    def __str__(self):
        return "{} - PK: {}".format(__name__, self.pk)


class ActivatableModel(BaseModelMixin):
    active = models.BooleanField(verbose_name=_(
        "Status"), null=False, blank=True, default=True)
    active_at = models.DateTimeField(
        verbose_name=_("Active at"), null=True, blank=True)
    inactive_at = models.DateTimeField(
        verbose_name=_("Inactive at"), null=True, blank=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(ActivatableModel, self).__init__(*args, **kwargs)
        self.pre_active = self.active

    def set_active(self):
        self.active = True
        self.save(update_fields=["active"])

    def set_inactive(self):
        self.active = False
        self.save(update_fields=["active"])

    def save(self, *args, **kwargs):
        if self.pk:
            if self.pre_active != self.active:
                if self.active:
                    self.active_at = timezone.now()
                    self.on_activation()
                else:
                    self.inactive_at = timezone.now()
                    self.on_desactivation()
        else:
            if self.active:
                self.active_at = timezone.now()
        super(ActivatableModel, self).save(*args, **kwargs)
        self.pre_active = self.active

    def on_activation(self):
        pass

    def on_desactivation(self):
        pass


class DummyActivatableModel(ActivatableModel):
    pass


class ActivatableOrderableModel(Orderable, ActivatableModel):
    sort_order = models.IntegerField(verbose_name=_(
        "Order value"), unique=True, blank=True, null=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        model = type(self)
        if self.sort_order is None:
            instances = model.objects.all().order_by("-sort_order")
            index = 1
            if instances.count() != 0:
                index = instances.first().sort_order + 1
            self.sort_order = index
        else:
            instances = model.objects.filter(sort_order=self.sort_order)
            if instances.count() != 0:
                instance = instances.first()
                instance.sort_order += 1
                instance.save()
        super(ActivatableOrderableModel, self).save(*args, **kwargs)


class DummyActivatableOrderableModel(ActivatableOrderableModel):
    pass


class ScheduledActivatableOrderableModel(ActivatableOrderableModel):
    publish_date = models.DateTimeField(
        verbose_name=_("Publish Date"), null=False, blank=True, default=timezone.now)
    unpublish_date = models.DateTimeField(
        verbose_name=_("Unpublished Date"), null=True, blank=True)

    class Meta:
        abstract = True

    def publish(self):
        self.active = True
        self.save(update_fields=["active"])

    def unpublish(self):
        self.active = False
        self.save(update_fields=["active"])


class ScheduleChanges(ActivatableModel):
    pre_changes_info = models.TextField(
        verbose_name=_("Pre changes"), null=False, blank=False)
    pos_changes_info = models.TextField(
        verbose_name=_("Pos changes"), null=False, blank=False)
    start_at = models.DateTimeField(
        verbose_name=_("Start at"), null=False, blank=False)
    end_at = models.DateTimeField(
        verbose_name=_("End at"), null=True, blank=True)
    applied_changes = models.BooleanField(
        verbose_name=_("Applied Changes"), default=False)
    reverted_changes = models.BooleanField(
        verbose_name=_("Reverted Changes"), default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    @staticmethod
    def schedule_change(obj, changed_obj, start_at, end_at=None,  fields="__all__"):
        obj_type = type(obj)
        changed_obj = type(obj)

        if obj_type != changed_obj:
            raise Exception(
                "To create a schedule the both objects must be equals")

        now = timezone.now()
        if start_at <= now:
            raise Exception("Cant have a date to change bigger than now.")
        if end_at is not None:
            if start_at >= end_at:
                raise Exception("End at must be bigger than start at")

        pre_changes_info = None
        pos_changes_info = None
        if fields == "__all__":
            pre_changes_info = serializers.serialize("json", [obj])
            pos_changes_info = serializers.serialize("json", [changed_obj])
        else:
            pre_changes_info = serializers.serialize(
                "json", [obj], fields=fields)
            pos_changes_info = serializers.serialize(
                "json", [changed_obj], fields=fields)

        instance = ScheduleChanges(pre_changes_info=pre_changes_info, pos_changes_info=pos_changes_info,
                                   start_at=start_at, end_at=end_at, content_object=obj)
        instance.save()

    def apply(self):
        self._apply_changes(self.pos_changes_info)

    def revert(self):
        self._apply_changes(self.pre_changes_info)

    def _apply_changes(self, changes_info):
        fields = json.loads(changes_info)[0]["fields"].keys()
        generator = serializers.deserialize(
            "json", changes_info, ignorenonexistent=True)

        for deserialized_obj in generator:
            for field in fields:
                setattr(self, field, getattr(deserialized_obj.object, field))

        self.save()

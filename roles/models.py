from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import ActivatableModel, BaseModelMixin
from wagtail.admin.edit_handlers import FieldPanel


# Create your models here.
class Service(ActivatableModel):
    identifier = models.CharField(verbose_name=_(
        "identifier"), null=False, blank=False, max_length=256)
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=128)

    panels = [
        FieldPanel('identifier'),
        FieldPanel('name'),
        FieldPanel('active'),
    ]


class Role(ActivatableModel):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=128)
    services = models.ManyToManyField("Service", through="ServiceRole")

    panels = [
        FieldPanel('name'),
        FieldPanel('active'),
    ]


class ServiceRole(BaseModelMixin):
    role = models.ForeignKey(
        Role, null=False, blank=False, on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, null=False, blank=False, on_delete=models.CASCADE)
    external_identifier = models.CharField(verbose_name=_(
        "External identifier"), null=False, blank=False, max_length=256)

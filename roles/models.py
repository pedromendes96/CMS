from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import ActivatableModel, BaseModelMixin
from wagtail.admin.edit_handlers import FieldPanel
from client.models import ServiceInfo


# Create your models here
class Role(ActivatableModel):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=128)
    services = models.ManyToManyField(
        "client.ServiceInfo", through="ServiceRole")

    panels = [
        FieldPanel('name'),
        FieldPanel('active'),
    ]


class ServiceRole(ActivatableModel):
    role = models.ForeignKey(
        Role, null=False, blank=False, on_delete=models.CASCADE)
    service = models.ForeignKey(
        ServiceInfo, null=False, blank=False, on_delete=models.CASCADE)
    external_identifier = models.CharField(verbose_name=_(
        "External identifier"), null=False, blank=False, max_length=256)

    panels = [
        FieldPanel('role'),
        FieldPanel('service'),
        FieldPanel('active'),
    ]

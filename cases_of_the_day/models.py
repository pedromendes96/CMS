from polymorphic.models import PolymorphicModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page
from utils.models import ActivatableOrderableModel

# Create your models here.


class LocatedModel(PolymorphicModel, ActivatableOrderableModel):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=64)
    latitude = models.FloatField(verbose_name=_(
        "Latitude"), null=False, blank=False)
    longitude = models.FloatField(verbose_name=_(
        "Longitude"), null=False, blank=False)
    zoom = models.IntegerField(verbose_name=_("Zoom"), null=False, blank=False)


class CasesOfTheDay(LocatedModel):
    date = models.DateField(verbose_name=_("Date"), null=False, blank=False)
    time = models.TimeField(verbose_name=_("Time"), null=False, blank=False)
    media = models.ForeignKey("multimedia.Media", verbose_name=_(
        "Media"), null=False, blank=False, on_delete=models.CASCADE)


class Region(LocatedModel):
    symbol = models.ImageField(verbose_name=_("Symbol"), null=True, blank=True)


class Locals(LocatedModel):
    district = models.ForeignKey(
        Region, null=False, blank=False, on_delete=models.CASCADE)

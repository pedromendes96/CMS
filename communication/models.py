from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from utils.models import BaseModelMixin, ActivatableModel

User = get_user_model()
# Create your models here.


class EmailMessage(BaseModelMixin):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    sent = models.BooleanField(verbose_name=_("Sent"), default=False)
    sent_at = models.DateTimeField(verbose_name=_(
        "Sent at"), null=True, blank=True, default=None)
    opened = models.BooleanField(verbose_name=_("Opened"), default=False)
    clicked = models.BooleanField(verbose_name=_("Clicked"), default=False)


class MetaData(models.Model):
    user_agent = models.CharField(verbose_name=_("User Agent"))
    ip = models.GenericIPAddressField(verbose_name=_("Ip"))


class Opening(models.Model):
    email = models.ForeignKey(EmailMessage, null=False, blank=False)
    opened_at = models.DateTimeField(
        verbose_name=_("Opened at"), auto_now_add=True)
    metadata = models.ForeignKey(MetaData, null=True, blank=True)


class Clicking(models.Model):
    email = models.ForeignKey(EmailMessage, null=False, blank=False)
    link = models.TextField(verbose_name=_("Link"), null=False, blank=False)
    click_at = models.DateTimeField(
        verbose_name=_("Opened at"), auto_now_add=True)
    metadata = models.ForeignKey(MetaData, null=True, blank=True)

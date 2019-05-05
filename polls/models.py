from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable
from utils.models import ActivatableOrderableModel, BaseModelMixin, ScheduledActivatableOrderableModel

User = get_user_model()

# Create your models here.


class Poll(ClusterableModel, ScheduledActivatableOrderableModel):
    question = models.CharField(verbose_name=_(
        "Question"), max_length=256, null=False, blank=False)

    panels = [
        FieldPanel("question"),
        FieldPanel("active"),
        FieldPanel("publish_date"),
        FieldPanel("unpublish_date"),
        InlinePanel("option", label=_("Options")),
    ]

    def get_options(self):
        return Option.objects.filter(poll=self, active=True)


class Option(ActivatableOrderableModel):
    label = models.CharField(verbose_name=_(
        "label"), max_length=256, null=False, blank=False)
    poll = ParentalKey(
        Poll, on_delete=models.CASCADE, blank=False, null=False, related_name="option", related_query_name="option")
    img = models.ImageField(verbose_name=_("Image"), null=True, blank=True)

    panels = [
        FieldPanel("label"),
        FieldPanel("img"),
        FieldPanel("active"),
    ]

    def get_percentage(self):
        return float(Vote.objects.filter(option=self).count()) / float(Vote.objects.filter(option__poll=self.poll, option__active=True).count())


class Vote(BaseModelMixin):
    option = models.ForeignKey(
        Option, null=False, blank=False, on_delete=models.CASCADE)
    by_offline_user = models.BooleanField(verbose_name=_(
        "By a offline user"), null=False, blank=False)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

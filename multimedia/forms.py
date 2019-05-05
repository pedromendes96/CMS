from wagtail.admin.forms import WagtailAdminModelForm
from django.forms import ModelMultipleChoiceField
from django.utils import timezone
from django.utils.translation import gettext as _


class FacebookStreamForm(WagtailAdminModelForm):
    def is_valid(self):
        if super().is_valid():
            if self.cleaned_data["is_scheduled"]:
                if self.cleaned_data["planned_start"] < timezone.now():
                    self.add_error("planned_start", ValueError(
                        _("Must be a date bigger than now")))
                    return False
            return True
        return False

    def save(self, *args, **kwargs):
        from .models import FacebookLiveStreamGroup, FacebookLiveStreamPage
        instance = super().save(*args, **kwargs)
        facebook_groups = FacebookLiveStreamGroup.objects.filter(
            facebook_stream=instance)
        facebook_pages = FacebookLiveStreamPage.objects.filter(
            facebook_stream=instance)

        self._update_is_live(instance, facebook_groups)
        self._update_is_live(instance, facebook_pages)

        return instance

    def _update_is_live(self, instance, object_list):
        for obj in object_list:
            if obj.is_live != instance.is_live:
                obj.is_live = instance.is_live
                obj.save(update_fields=["is_live"])

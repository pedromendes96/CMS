from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, FieldPanel

# Create your models here.
@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    facebook_access_token = models.CharField(
        verbose_name=_("Facebook access token"), max_length=64)
    facebook_page_id = models.CharField(verbose_name=_(
        "Facebook Page Id"), max_length=256, null=True, blank=True)
    instagram = models.URLField(help_text='Your Instagram URL')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')

    panels = [
        FieldPanel('facebook'),
        FieldPanel('facebook_access_token'),
        FieldPanel('facebook_page_id'),
        FieldPanel('instagram'),
        FieldPanel('youtube'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading=_('Social Media Settings'))
    ])


@register_setting
class APISettings(BaseSetting):
    google_maps_key = models.CharField(verbose_name=_(
        "Google Maps Key"), max_length=256, null=False, blank=False)


@register_setting
class TelephoneContactSettings(BaseSetting):
    geral_contact_telephone = models.CharField(
        verbose_name=_("Geral Telephone"), null=False, blank=False, max_length=32)
    secretariat_contact_telephone = models.CharField(
        verbose_name=_("Secretariat Telephone"), null=False, blank=False, max_length=32)
    geral_contact_telephone = models.CharField(
        verbose_name=_("Geral Telephone"), null=False, blank=False, max_length=32)

    panels = [
        FieldPanel('geral_contact_telephone'),
        FieldPanel('secretariat_contact_telephone'),
        FieldPanel('geral_contact_telephone'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading=_('Telephone contacts Settings'))
    ])


@register_setting
class EmailSettings(BaseSetting):
    readers_letter_email = models.CharField(
        verbose_name=_("Reader's letter email"), null=False, blank=False, max_length=64)
    redaction_email = models.CharField(verbose_name=_(
        "Redaction Email"), null=False, blank=False, max_length=64)
    publish_email = models.CharField(verbose_name=_(
        "Publish Email"), null=False, blank=False, max_length=64)

    panels = [
        FieldPanel('readers_letter_email'),
        FieldPanel('redaction_email'),
        FieldPanel('publish_email'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading=_('Emails contacts Settings'))
    ])


@register_setting
class EnterpriseSettings(BaseSetting):
    street = models.CharField(verbose_name=_(
        "Street"), null=False, blank=False, max_length=32)
    zip_code = models.CharField(verbose_name=_(
        "Street"), null=False, blank=False, max_length=32)
    city = models.CharField(verbose_name=_(
        "City"), null=False, blank=False, max_length=32)
    country = models.CharField(verbose_name=_(
        "Country"), null=False, blank=False, max_length=32)

    panels = [
        FieldPanel('street'),
        FieldPanel('zip_code'),
        FieldPanel('city'),
        FieldPanel('country'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading=_('Enterprise Settings'))
    ])


@register_setting
class ExternalServiceSettings(BaseSetting):
    liveblog_url = models.URLField(verbose_name=_("Liveblog Url"))
    initiatives_url = models.URLField(verbose_name=_("Initiatives Url"))
    editions_url = models.URLField(verbose_name=_("Editions Url"))
    subscriptions_url = models.URLField(verbose_name=_("Subscriptions Url"))
    malta_url = models.URLField(verbose_name=_("Malta Url"))
    dcs_url = models.URLField(verbose_name=_("DCS URL"))
    magazine_D7_url = models.URLField(verbose_name=_("Magazine D7 Url"))

    panels = [
        FieldPanel('liveblog_url'),
        FieldPanel('initiatives_url'),
        FieldPanel('editions_url'),
        FieldPanel('subscriptions_url'),
        FieldPanel('malta_url'),
        FieldPanel('magazine_D7_url'),
        FieldPanel('dcs_url'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading=_('Enterprise Settings'))
    ])

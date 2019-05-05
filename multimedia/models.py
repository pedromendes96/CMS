from .forms import FacebookStreamForm
from polymorphic.models import PolymorphicModel
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from utils.models import ActivatableOrderableModel
from taxonomy.models import Section
from taggit.managers import TaggableManager
from site_settings.models import SocialMediaSettings
from utils.models import ActivatableModel, BaseModelMixin
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.edit_handlers import FieldPanel, ObjectList, InlinePanel, MultiFieldPanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
import requests
import logging

LIVE_NOW = "LIVE_NOW"
INGEST_STREAMS = "ingest_streams"
VOD = "VOD"
ERRORS = "errors"
ACCESS_TOKEN = "access_token"
TITLE = "title"
DESCRIPTION = "description"
STATUS = "status"
END_LIVE_VIDEO = "end_live_video"
FIELDS = "fields"
ID = "id"
STREAM_URL = "stream_url"
SECURE_STREAM_URL = "secure_stream_url"
SCHEDULED_UNPUBLISHED = "SCHEDULED_UNPUBLISHED"
PLANNED_START_TIME = "planned_start_time"
BROADCAST_STATUS = "broadcast_status"
TARGETING = "targeting"
GEO_LOCATIONS = "geo_locations"
QUESTION = "question"
OPTIONS = "options"
ACTION = "action"
CLOSE = "close"
SHOW_VOTING = "SHOW_VOTING"
POLL_OPTIONS = "poll_options"
TOTAL_VOTES = "total_votes"
SHOW_RESULTS = "SHOW_RESULTS"

logger = logging.getLogger("multimedia")

# ABSTRACT MODELS


class TagManagement(TaggedItemBase):
    content_object = ParentalKey(
        'multimedia.Media', related_name='tagged_items')


class ActivatableOrderableClusterableModel(ClusterableModel, ActivatableOrderableModel):
    class Meta:
        abstract = True


class Media(PolymorphicModel, ActivatableOrderableClusterableModel):
    url = models.URLField(verbose_name=_("Url"), null=False, blank=False)
    section = models.ForeignKey(
        Section, null=False, blank=False, on_delete=models.CASCADE)
    tags = ClusterTaggableManager(through=TagManagement, blank=True)
    show_in_home_page = models.BooleanField(
        verbose_name=_("Show in home page"), default=False)
    title = models.CharField(verbose_name=_(
        "Title"), max_length=64, null=False, blank=False)
    short_description = models.CharField(verbose_name=_(
        "Short description"), max_length=256, null=True, blank=True)


class FacebookEntity(BaseModelMixin):
    facebook_id = models.CharField(verbose_name=_(
        "Facebook Id"), null=True, blank=True, max_length=256)

    class Meta:
        abstract = True


class FacebookFormat(FacebookEntity):
    access_token = models.CharField(verbose_name=_(
        "Access token"), null=True, blank=True, max_length=256)

    class Meta:
        abstract = True


class Stream(Media):
    description = models.TextField(verbose_name=_(
        "Description"), null=True, blank=True)
    is_live = models.BooleanField(
        verbose_name=_("Is Live"), null=False, blank=False)
    is_scheduled = models.BooleanField(verbose_name=_(
        "Is Scheduled"), null=False, blank=True, default=False)
    planned_start = models.DateTimeField(
        verbose_name=_("Planned Start"), null=True, blank=True)

    class Meta:
        abstract = True

# concrete classes


class Video(Media):
    auto_play = models.BooleanField(
        verbose_name=_("Auto play"), null=False, blank=False)

    panels = [
        FieldPanel("url"),
        FieldPanel("section"),
        FieldPanel("tags"),
        FieldPanel("show_in_home_page"),
        FieldPanel("title"),
        FieldPanel("short_description"),
        FieldPanel("auto_play"),
    ]


class FacebookGroup(FacebookFormat):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=128)

    panels = [
        FieldPanel("facebook_id"),
        FieldPanel("name"),
        FieldPanel("access_token")
    ]


class FacebookPage(FacebookFormat):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=128)

    panels = [
        FieldPanel("facebook_id"),
        FieldPanel("name"),
        FieldPanel("access_token")
    ]


class FacebookStream(Stream):

    panels = [
        FieldPanel("url"),
        FieldPanel("title"),
        FieldPanel("short_description"),
        FieldPanel("description"),
        FieldPanel("is_live"),
        FieldPanel("is_scheduled"),
        FieldPanel("show_in_home_page"),
        FieldPanel("section"),
        FieldPanel("planned_start"),
        FieldPanel("tags"),
        MultiFieldPanel(
            [InlinePanel("stream_group_relationship")], heading=_("Groups")),
        MultiFieldPanel(
            [InlinePanel("stream_page_relationship")], heading=_("Pages")),
    ]

    edit_handler = ObjectList(panels, base_form_class=FacebookStreamForm)

    def get_embed_code(self):
        pass

    def start(self):
        streaming_pages = FacebookLiveStreamPage.objects.filter(
            facebook_stream=self)
        streaming_groups = FacebookLiveStreamGroup.objects.filter(
            facebook_stream=self)

        for streaming_page in streaming_pages:
            streaming_page.start()

        for streaming_group in streaming_groups:
            streaming_group.start()

    def end(self):
        streaming_pages = FacebookLiveStreamPage.objects.filter(
            facebook_stream=self)
        streaming_groups = FacebookLiveStreamGroup.objects.filter(
            facebook_stream=self)

        for streaming_page in streaming_pages:
            streaming_page.end()

        for streaming_group in streaming_groups:
            streaming_group.end()


class FacebookPoll(FacebookEntity):
    question = models.CharField(verbose_name=_(
        "Question"), null=False, blank=False, max_length=256)

    panels = [
        FieldPanel("question"),
    ]

    def open(self):
        url = "https://graph.facebook.com/{}/polls".format(
            self.facebook_id)
        options = self.options.all()
        response = requests.post(url, data={
            QUESTION: self.question,
            OPTIONS: [option.name for option in options],
            ACCESS_TOKEN: self.get_access_token()
        })

    def reopen(self):
        url = "https://graph.facebook.com/{}".format(
            self.facebook_id)
        response = requests.post(url, data={
            ACTION: CLOSE,
            ACCESS_TOKEN: self.get_access_token()
        })
        self.facebook_id = response.json()["id"]
        self.save()

    def close(self):
        url = "https://graph.facebook.com/{}".format(
            self.facebook_id)
        response = requests.post(url, data={
            ACTION: SHOW_VOTING,
            ACCESS_TOKEN: self.get_access_token()
        })

    def show_closed_results(self):
        url = "https://graph.facebook.com/{}".format(
            self.facebook_id)
        response = requests.post(url, data={
            ACTION: SHOW_RESULTS,
            ACCESS_TOKEN: self.get_access_token()
        })

    def get_settings(self):
        url = "https://graph.intern.facebook.com/{}".format(
            self.facebook_id)
        response = requests.get(url, params={
            FIELDS: POLL_OPTIONS,
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def get_all_votes(self):
        url = "https://graph.intern.facebook.com/{}".format(self.facebook_id)
        response = requests.get(url, params={
            FIELDS: POLL_OPTIONS+"{text,total_votes}",
            ACCESS_TOKEN: self.access_token()
        })
        return response.json()


class FacebookOption(FacebookEntity):
    name = models.CharField(verbose_name=_("Option"),
                            null=False, blank=False, max_length=256)
    poll = models.ForeignKey(FacebookPoll, null=False,
                             blank=False, on_delete=models.CASCADE)

    def get_votes(self):
        url = "https://graph.facebook.com/{}".format(self.facebook_id)
        response = requests.get(url, params={
            FIELDS: TOTAL_VOTES,
            ACCESS_TOKEN: self.poll.get_access_token()
        })
        return response[TOTAL_VOTES]

    panels = [
        FieldPanel("name"),
    ]


class FacebookStreamRelation(ActivatableModel):
    active = models.BooleanField(verbose_name=_(
        "Status"), null=False, blank=True, default=False)
    stream_url = models.TextField(verbose_name=_(
        "Stream url"), null=True, blank=True)
    secure_stream_url = models.TextField(
        verbose_name=_("Stream url"), null=True, blank=True)
    stream_id = models.CharField(verbose_name=_(
        "Stream ID"), null=True, blank=True, max_length=128)
    is_live = models.BooleanField(verbose_name=_(
        "Is Live"), null=False, blank=True, default=False)
    is_scheduled = models.BooleanField(verbose_name=_(
        "Is Scheduled"), null=False, blank=True, default=False)
    poll = models.ForeignKey(FacebookPoll, null=True,
                             blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def start(self):
        logger.info("Starting the live video in the service with the access_token: {}".format(
            self.get_facebook_id()))
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.post(url, data={
            TITLE: self.facebook_stream.title,
            DESCRIPTION: self.facebook_stream.description,
            ACCESS_TOKEN: self.get_access_token(),
            STATUS: LIVE_NOW
        })
        data = response.json()
        self.stream_id = data.get(ID)
        self.stream_url = data.get(STREAM_URL)
        self.secure_stream_url = data.get(SECURE_STREAM_URL)
        self.is_live = True
        self.save()

        self.set_as_embeddable()

    def set_as_embeddable(self):
        url = "https://graph.facebook.com/{}".format(self.stream_id)
        data = {
            "embeddable": True,
            "access_token": self.get_access_token()
        }
        response = requests.post(url, data=data)

    def get_embeddable_code(self):
        url = "https://graph.facebook.com/{}".format(self.stream_id)
        data = {
            "fields": "embed_html",
            "access_token": self.get_access_token()
        }
        response = requests.post(url, data=data)
        return response.json()["embed_html"]

    def end(self):
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.post(url, data={
            ACCESS_TOKEN: self.get_access_token(),
            END_LIVE_VIDEO: True
        })
        self.is_live = False
        self.save()

    def is_live_now(self):
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.get(url)
        data = response.json()
        return data[STATUS] != self.VOD

    def delete_from_facebook(self):
        url = "https://graph.facebook.com/{}".format(self.get_facebook_id())
        response = requests.delete(url, params={
            ACCESS_TOKEN: self.get_access_token()
        })

    def get_error_code_information(self):
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.get(url, params={
            FIELDS: ERRORS,
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def get_access_token(self):
        return ""

    def get_facebook_id(self):
        return ""

    def get_status(self):
        url = "https://graph.facebook.com/{}".format(self.stream_id)
        response = requests.get(url, params={
            FIELDS: INGEST_STREAMS,
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def schedule(self, timestamp):
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.post(url, data={
            STATUS: SCHEDULED_UNPUBLISHED,
            PLANNED_START_TIME: timestamp,
            ACCESS_TOKEN: self.get_access_token()
        })

    def reschedule(self, timestamp):
        url = "https://graph.facebook.com/{}".format(self.stream_id)
        response = requests.post(url, data={
            PLANNED_START_TIME: timestamp,
            ACCESS_TOKEN: self.get_access_token()
        })

    def get_scheduled_live_videos(self):
        url = "https://graph.facebook.com/{}/live_videos".format(
            self.get_facebook_id())
        response = requests.get(url, params={
            BROADCAST_STATUS: SCHEDULED_UNPUBLISHED,
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def start_scheduled_now(self):
        url = "https://graph.facebook.com/{}".format(self.stream_id)
        response = requests.post(url, data={
            STATUS:  LIVE_NOW,
            ACCESS_TOKEN: self.get_access_token()
        })

    def get_comments(self):
        url = "https://graph.facebook.com/{}/comments".format(
            self.get_facebook_id())
        response = requests.get(url, params={
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def get_reactions(self):
        url = "https://graph.facebook.com/{}/reactions".format(
            self.get_facebook_id())
        response = requests.get(url, params={
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()

    def set_targeting(self, age_restriction=None, geo_locations_restriction=None):
        url = "https://graph.facebook.com/{}".format(self.get_facebook_id())

        data = dict()

        if age_restriction:
            data = age_restriction
        if geo_locations_restriction:
            data[GEO_LOCATIONS] = geo_locations_restriction

        response = requests.post(url, data=data)

    def get_audience_information(self):
        url = "https://graph.facebook.com/{}".format(self.get_facebook_id())
        response = requests.get(url, params={
            FIELDS: TARGETING,
            ACCESS_TOKEN: self.get_access_token()
        })
        return response.json()


class FacebookLiveStreamGroup(FacebookStreamRelation):
    facebook_group = models.ForeignKey(
        FacebookGroup, null=False, blank=False, on_delete=models.CASCADE)
    facebook_stream = ParentalKey(
        FacebookStream, null=False, blank=False, on_delete=models.CASCADE, related_name="stream_group_relationship")

    panels = [
        FieldPanel("facebook_group")
    ]

    def get_access_token(self):
        return self.facebook_group.access_token

    def get_facebook_id(self):
        return self.facebook_group.facebook_id


class FacebookLiveStreamPage(FacebookStreamRelation):
    facebook_page = models.ForeignKey(
        FacebookPage, null=False, blank=False, on_delete=models.CASCADE)
    facebook_stream = ParentalKey(
        FacebookStream, null=False, blank=False, on_delete=models.CASCADE, related_name="stream_page_relationship")

    panels = [
        FieldPanel("facebook_page")
    ]

    def get_access_token(self):
        return self.facebook_page.access_token

    def get_facebook_id(self):
        return self.facebook_page.facebook_id

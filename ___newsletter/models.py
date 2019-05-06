from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.search import index

from taxonomy.models import Category
from users.models import NewsletterAuthor
from utils.models import BaseModelMixin, ActivatableModel

import logging

User = get_user_model()

logger = logging.getLogger("newsletter")

# Create your models here.


class Newsletter(ActivatableModel):
    DAILY = "daily"
    WEEKLY = "weekly"

    title = models.CharField(verbose_name=_(
        "Title"), null=False, blank=False, max_length=128)
    frequency = models.CharField(verbose_name=_("Frequency"), max_length=32, null=False, blank=False, choices=(
        (DAILY, _("Daily")),
        (WEEKLY, _("Weekly")),
    ))
    description = models.TextField(verbose_name=_(
        "Description"), null=False, blank=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE,
                                 related_name="newsletters", related_query_name="newsletters")
    users = models.ManyToManyField(User, through="NewsletterSubscription")

    def subscribe(self, user):
        newsletter_subscriptions = NewsletterSubscription.objects.filter(
            user=user, newsletter=self)
        if newsletter_subscriptions.count() == 0:
            instance = NewsletterSubscription.objects.create(
                user=user, newsletter=self)
        else:
            instance = newsletter_subscriptions.first()
            instance.active = True
            instance.save(update_fields=["active"])
        logger.info("User with the email {} subscribed to the newsletter {}-{}".format(
            user.email, self.pk, self.title))

    def subscribe_with_email(self, email):
        users = User.objects.filter(email=email)

    def unsubscribe(self, user):
        newsletter_subscriptions = NewsletterSubscription.objects.filter(
            user=user, newsletter=self)
        if newsletter_subscriptions.count() > 0:
            instance = newsletter_subscriptions.first()
            instance.active = False
            instance.save(update_fields=["active"])
        logger.info("User with the email {} unsubscribed to the newsletter {}-{}".format(
            user.email, self.pk, self.title))


class NewsletterSubscription(ActivatableModel):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE,
                             related_name="newsletter_subscription",
                             related_query_name="newsletter_subscription")
    newsletter = models.ForeignKey(Newsletter, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name="newsletter_subscription", related_query_name="newsletter_subscription")


class Template(Page, BaseModelMixin):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]


class NewsletterMessage(BaseModelMixin):
    author = models.ForeignKey(NewsletterAuthor, verbose_name=_("User"), null=False, blank=False,
                               on_delete=models.CASCADE, related_name="messages",
                               related_query_name="messages")
    newsletter = models.ForeignKey(Newsletter, verbose_name=_("Newsletter"), null=False, blank=False,
                                   on_delete=models.CASCADE, related_name="messages",
                                   related_query_name="messages")
    template = models.ForeignKey("newsletter.Template", verbose_name=_("User"), null=True, blank=True,
                                 on_delete=models.CASCADE, related_name="message",
                                 related_query_name="message")
    status = models.CharField(verbose_name=_("Status"), max_length=32, blank=False, null=False, choices=(
        ("draft", _("Draft")),
        ("sent", _("Sent"))
    ), default="draft")
    users = models.ManyToManyField(User, through="NewsletterMessageUser")

    def send_to_subscribers(self):
        newsletter_subscriptions = NewsletterSubscription.objects.filter(
            newsletter=self.newsletter)
        for instance in newsletter_subscriptions:
            instance = NewsletterMessageUser(
                newsletter_message=self, user=instance.user)
            instance.save()
            instance.send()


class NewsletterMessageUser(BaseModelMixin):
    newsletter_message = models.ForeignKey("newsletter.NewsletterMessage", null=False, blank=False,
                                           on_delete=models.CASCADE, related_name="message_user",
                                           related_query_name="message_user")
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="message",
                             related_query_name="message")
    # email = models.ForeignKey("dms.DMSEmailMessage", null=False, blank=False, on_delete=models.CASCADE)

    def send(self):
        logger.info(
            "Sending the email with the newsletter to the user {}".format(self.user.email))

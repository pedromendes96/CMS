from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.core.blocks import BlockQuoteBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtail.contrib.table_block.blocks import TableBlock
from taxonomy.models import Category
from users.models import Reporter, OpinionArticleAuthor
from utils.models import ActivatableModel
from .blocks.image import Carousel, ImageSlider
from .blocks.charts import LineChart, SegmentChart, BarChart
from .blocks.localization import GoogleMapBlock
from .blocks.social import FacebookPostEmbed, FacebookVideoEmbed, InstagramEmbed, PinterestBoardEmbed, PinterestPinEmbed, PinterestProfileEmbed
from wagtailmetadata.models import MetadataPageMixin


class Role(ActivatableModel):
    name = models.CharField(verbose_name=_(
        "Name"), null=False, blank=False, max_length=32)

    def __str__(self):
        return self.name

# Abstract models


class AbstractArticle(ActivatableModel):
    categories = models.ManyToManyField(Category)
    roles = models.ManyToManyField(Role)
    status = models.CharField(verbose_name=_("Status"), max_length=32, null=True, blank=True, choices=(
        ("draft", _("Draft")),
        ("finished", _("Finished")),
        ("updated", _("Updated"))
    ))
    mobile_content = models.TextField(
        verbose_name=_("Mobile Info"), null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('categories'),
        index.SearchField('status'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('categories'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]

    api_fields = [
        APIField('categories'),
        APIField('have_paywall'),
        APIField('mobile_content'),
    ]

    class Meta:
        abstract = True


class AbstractReporterArticle(Page, AbstractArticle):
    author = models.ForeignKey(Reporter, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="articles",
                               related_query_name="articles")
    is_spotlight = models.BooleanField(verbose_name=_(
        "IS spotlight"), blank=False, null=False, default=False)

    search_fields = AbstractArticle.search_fields + [
        index.SearchField('author'),
        index.SearchField('is_spotlight'),
    ]

    content_panels = AbstractArticle.content_panels + [
        FieldPanel('is_spotlight'),
    ]

    api_fields = AbstractArticle.api_fields + [
        APIField('author'),
        APIField('is_spotlight'),
    ]

    class Meta:
        abstract = True


class AbstractOpinionArticle(Page, AbstractArticle):
    author = models.ForeignKey(OpinionArticleAuthor, null=False, blank=False, on_delete=models.DO_NOTHING,
                               related_query_name="option_articles", related_name="option_articles")

    search_fields = AbstractArticle.search_fields + [
        index.SearchField('author')
    ]

    api_fields = AbstractArticle.api_fields + [
        APIField('author')
    ]

    class Meta:
        abstract = True


# Concrete models

class BasicReporterArticle(AbstractReporterArticle):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('blockquote', BlockQuoteBlock()),
        ('embed', EmbedBlock()),
        ('carousel', Carousel()),
        ('slider', ImageSlider()),
        ('linechart', LineChart()),
        ('barchart', BarChart()),
        ('segmentchart', SegmentChart()),
        ('googlemap', GoogleMapBlock()),
        ('table', TableBlock()),
        ('facebookpost', FacebookPostEmbed()),
        ('facebookvideo', FacebookVideoEmbed()),
        ('instagram', InstagramEmbed()),
        ('pinterestboard', PinterestBoardEmbed()),
        ('pinterestpin', PinterestPinEmbed()),
        ('pinterestprofile', PinterestProfileEmbed()),
        ('pagechooser', blocks.PageChooserBlock())
    ])

    parent_page_types = ['home.HomePage']

    search_fields = AbstractReporterArticle.search_fields + [
        index.SearchField('body'),
    ]

    # Editor panels configuration

    content_panels = AbstractReporterArticle.content_panels + [
        StreamFieldPanel('body'),
    ]

    api_fields = AbstractReporterArticle.api_fields + [
        APIField('body')
    ]


class BasicOpinionArticle(AbstractOpinionArticle):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('table', TableBlock()),
        ('blockquote', BlockQuoteBlock()),
        ('embed', EmbedBlock()),
        ('carousel', Carousel())
    ])

    search_fields = AbstractOpinionArticle.search_fields + [
        index.SearchField('body'),
    ]

    # Editor panels configuration

    content_panels = AbstractOpinionArticle.content_panels + [
        StreamFieldPanel('body'),
    ]

    api_fields = AbstractOpinionArticle.api_fields + [
        APIField('body')
    ]

    parent_page_types = ['home.HomePage']

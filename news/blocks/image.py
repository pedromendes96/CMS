from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class LabeledImage(blocks.StructBlock):
    label = blocks.CharBlock()
    img = ImageChooserBlock()

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-image'
        label = _("Labeled Image")


class ImageSlider(blocks.StructBlock):
    old_image = LabeledImage()
    new_image = LabeledImage()

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-image'
        label = _("Image Slider")


class Quotation(blocks.StructBlock):
    text = blocks.TextBlock()
    author = blocks.CharBlock()


class ContentCarousel(blocks.StructBlock):
    img = ImageChooserBlock()
    quotation = Quotation()
    video = EmbedBlock()


class Carousel(blocks.StreamBlock):
    element = ContentCarousel()

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-image'
        label = _("Image Carousel")

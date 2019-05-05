from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.apps import apps
from django.utils.translation import gettext_lazy as _


class InfoWindowBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock()
    paragraph = blocks.TextBlock()


class MarkerBlock(blocks.StructBlock):
    latitude = blocks.FloatBlock()
    longitude = blocks.FloatBlock()
    content = InfoWindowBlock(required=False)

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-map-marker'
        label = _("Marker")


class GoogleMapBlock(blocks.StructBlock):
    latitude = blocks.DecimalBlock(max_digits=6)
    longitude = blocks.DecimalBlock(max_digits=6)
    zoom = blocks.IntegerBlock()
    markers = blocks.ListBlock(MarkerBlock(), required=False)

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-map'
        label = _("Google Map")

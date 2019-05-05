from django import template

from news.blocks.localization import GoogleMapBlock

register = template.Library()


@register.simple_tag
def have_google_maps_block(cls_list):
    return GoogleMapBlock in cls_list


@register.simple_tag
def is_a_google_maps_block(block):
    return isinstance(block, GoogleMapBlock)

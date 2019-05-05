from django import template
from news.blocks.image import ImageSlider

register = template.Library()


@register.simple_tag
def have_image_slider_block(cls_list):
    return ImageSlider in cls_list


@register.simple_tag
def is_image_slider_block(block):
    return isinstance(block, ImageSlider)

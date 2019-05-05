import datetime
from django import template
from news.blocks.social import PinterestBoardEmbed, PinterestProfileEmbed, PinterestPinEmbed, FacebookPostEmbed, FacebookVideoEmbed, InstagramEmbed

register = template.Library()


@register.simple_tag
def get_sizes_pinterest(instance):
    instance_type = type(instance.block)
    return instance_type.SIZES_TO_VERBOSE.get(instance.value["size"], instance_type.DEFAULT)


@register.simple_tag
def have_facebook_block(cls_list):
    return FacebookPostEmbed in cls_list or FacebookVideoEmbed in cls_list


@register.simple_tag
def is_a_facebook_post_block(block):
    return isinstance(block, FacebookPostEmbed)


@register.simple_tag
def is_a_facebook_video_block(block):
    return isinstance(block, FacebookVideoEmbed)


@register.simple_tag
def have_instagram_block(cls_list):
    return InstagramEmbed in cls_list


@register.simple_tag
def is_a_instagram_block(block):
    return isinstance(block, InstagramEmbed)


@register.simple_tag
def is_a_pinterest_board_block(block):
    return isinstance(block, PinterestBoardEmbed)


@register.simple_tag
def is_a_pinterest_profile_block(block):
    return isinstance(block, PinterestProfileEmbed)


@register.simple_tag
def is_a_pinterest_pin_block(block):
    return isinstance(block, PinterestPinEmbed)


@register.simple_tag
def have_pinterest_block(cls_list):
    return PinterestBoardEmbed in cls_list or PinterestProfileEmbed in cls_list or PinterestPinEmbed in cls_list

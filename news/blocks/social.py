from wagtail.core import blocks
from django.apps import apps
from django.utils.translation import gettext_lazy as _


class InstagramEmbed(blocks.StructBlock):
    url = blocks.URLBlock()
    hide_caption = blocks.BooleanBlock(required=False)
    width = blocks.IntegerBlock(min_value=320)

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-instagram'
        label = _("Instagram Embed")


class FacebookPostEmbed(blocks.StructBlock):
    url = blocks.URLBlock()
    show_text = blocks.BooleanBlock(required=False)
    width = blocks.IntegerBlock(min_value=350, max_value=750, required=False)

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-facebook'
        label = _("Facebook Post Embed")


class FacebookVideoEmbed(blocks.StructBlock):
    url = blocks.URLBlock()
    allow_full_screen = blocks.BooleanBlock(required=False)
    auto_play = blocks.BooleanBlock(required=False)
    width = blocks.IntegerBlock(min_value=350, max_value=750, required=False)
    show_text = blocks.BooleanBlock(required=False)
    show_caption = blocks.BooleanBlock(required=False)

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-facebook'
        label = _("Facebook Video Embed")


class PinterestPinEmbed(blocks.StructBlock):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    SIZES_TO_VERBOSE = {
        SMALL: SMALL,
        MEDIUM: MEDIUM,
        LARGE: LARGE
    }
    url = blocks.URLBlock()
    size = blocks.ChoiceBlock(choices=(
        (SMALL, _("Small")),
        (MEDIUM, _("Medium")),
        (LARGE, _("Large"))
    ))
    hide_description = blocks.BooleanBlock()

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-pinterest'
        label = _("Pinterest Pin Embed")


class PinterestProfileEmbed(blocks.StructBlock):
    DEFAULT = {
        "data_pin_board_width": 400,
        "data_pin_scale_height": 240,
        "data_pin_scale_width": 80
    }
    SQUARE = "square"
    SIDEBAR = "sidebar"
    HEADER = "header"
    SIZES_TO_VERBOSE = {
        SQUARE: DEFAULT,
        SIDEBAR: {
            "data_pin_board_width": 150,
            "data_pin_scale_height": 800,
            "data_pin_scale_width": 60
        },
        HEADER: {
            "data_pin_board_width": 900,
            "data_pin_scale_height": 120,
            "data_pin_scale_width": 115
        }
    }
    url = blocks.URLBlock()
    size = blocks.ChoiceBlock(choices=(
        (SQUARE, _("Square")),
        (SIDEBAR, _("SideBar")),
        (HEADER, _("Header"))
    ))

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-pinterest'
        label = _("Pinterest Profile Embed")


class PinterestBoardEmbed(blocks.StructBlock):
    DEFAULT = {
        "data_pin_board_width": 400,
        "data_pin_scale_height": 240,
        "data_pin_scale_width": 80
    }
    SQUARE = "square"
    SIDEBAR = "sidebar"
    HEADER = "header"
    SIZES_TO_VERBOSE = {
        SQUARE: DEFAULT,
        SIDEBAR: {
            "data_pin_board_width": 150,
            "data_pin_scale_height": 800,
            "data_pin_scale_width": 60
        },
        HEADER: {
            "data_pin_board_width": 900,
            "data_pin_scale_height": 120,
            "data_pin_scale_width": 115
        }
    }
    url = blocks.URLBlock()
    size = blocks.ChoiceBlock(choices=(
        (SQUARE, _("Square")),
        (SIDEBAR, _("SideBar")),
        (HEADER, _("Header"))
    ))

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-pinterest'
        label = _("Pinterest Board Embed")

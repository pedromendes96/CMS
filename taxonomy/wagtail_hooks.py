from wagtail.core import hooks
from django.utils.text import slugify
from .admin import CategoryModelAdmin, SectionModelAdmin

import logging

logger = logging.getLogger("taxonomy")


@hooks.register('construct_main_menu')
def hide_explorer_menu_item_from_frank(request, menu_items):
    menu_items[:] = [
        item for item in menu_items if item.name != slugify(CategoryModelAdmin.menu_label) and item.name != slugify(SectionModelAdmin.menu_label)]

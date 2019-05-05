from datetime import datetime
from django import template
from django.utils import formats

register = template.Library()


@register.filter()
def attrs_for_table(row_object):
    variables = vars(row_object)
    if "order_key" in variables.keys():
        del variables["order_key"]
    return variables.keys()


@register.simple_tag
def get_object_attr(obj, key):
    if hasattr(obj, key):
        if isinstance(obj, datetime):
            return formats.date_format(obj, 'SHORT_DATETIME_FORMAT')
        else:
            return getattr(obj, key)
    else:
        return "-----"

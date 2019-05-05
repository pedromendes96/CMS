import datetime
from django import template
from news.blocks.charts import Chart, LineChart, BarChart, SegmentChart, SingleAxeChart, DoubleAxeChart

register = template.Library()


@register.simple_tag
def have_chart_block(cls_list):
    for cls in cls_list:
        if issubclass(cls, Chart):
            return True
    return False


@register.simple_tag
def is_chart_block(block):
    return isinstance(block, Chart)


@register.simple_tag
def is_line_chart(instance):
    return isinstance(instance, LineChart)


@register.simple_tag
def is_bar_chart(instance):
    return isinstance(instance, BarChart)


@register.simple_tag
def is_segment_chart(instance):
    return isinstance(instance, SegmentChart)


@register.simple_tag
def is_single_axe_chart(instance):
    return isinstance(instance, SingleAxeChart)


@register.simple_tag
def is_double_axe_chart(instance):
    return isinstance(instance, DoubleAxeChart)

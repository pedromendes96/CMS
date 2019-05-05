from wagtail.core import blocks
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class DataSetBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    color = blocks.CharBlock(min_length=7, max_length=7)
    data = blocks.ListBlock(blocks.CharBlock())


class DataColorBlock(blocks.StructBlock):
    color = blocks.CharBlock(min_length=7, max_length=7)
    data = blocks.CharBlock()


class DataSetMultipleColor(blocks.StructBlock):
    label = blocks.CharBlock()
    data_values = blocks.ListBlock(DataColorBlock())


class Chart(blocks.StructBlock):
    title = blocks.CharBlock()
    x_labels = blocks.ListBlock(blocks.CharBlock())


class SingleAxeChart(Chart):
    data_set = DataSetMultipleColor()


class DoubleAxeChart(Chart):
    data_sets = blocks.ListBlock(DataSetBlock())


class LineChart(DoubleAxeChart):
    x_label = blocks.CharBlock()
    y_label = blocks.CharBlock()

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-line-chart'
        label = _("Line Chart")


class BarChart(DoubleAxeChart):
    x_label = blocks.CharBlock()
    y_label = blocks.CharBlock()
    orientation = blocks.ChoiceBlock(choices=(
        ("horizontal", _("Horizontal")),
        ("vertical", _("Vertical"))
    ))

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-bar-chart'
        label = "Bar Chart"


class SegmentChart(SingleAxeChart):
    mode = blocks.ChoiceBlock(choices=(
        ("pie", _("Pie")),
        ("doughnut", _("Doughnut")),
    ))

    class Meta:
        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-pie-chart'
        label = _("Segment Chart")

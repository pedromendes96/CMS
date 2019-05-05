import logging
from abc import abstractmethod, ABC
from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.http.response import JsonResponse
from django.urls import reverse
from django.utils import formats
from polymorphic.models import PolymorphicModel

from .order_object import OrderObject

logger = logging.getLogger("administration")


class Process(ABC):

    def __init__(self, request):
        self.request = request
        self.draw = int(request.GET.get('draw', 0))
        self.length = int(request.GET.get('length', 10))
        self.start = int(request.GET.get('start', 0))
        self.order_column = int(request.GET.get('order[0][column]', '1'))
        self.order_direction = '-' if request.GET.get(
            'order[0][dir]', 'asc') == 'desc' else ''
        self.global_search = request.GET.get('search[value]', '')
        self.object_list = []
        self.number = 0

        # on click table row
        self.on_click_url = "#"
        self.extra_params = {}

        self.queryset = []
        self.id_prefix = self.get_id_prefix()

        # indexing stat
        self.is_orderable = False

        # datatable config
        self.buttons = []
        self.ajax_url = self.get_ajax_url()
        self.length_menu = self.set_menu_length()
        self.page_length = self.set_page_length()
        self.query_order = self.set_order()

        # thead elements
        self.thead = self.set_thead()
        self.searchable_fields = self.set_searchable()
        logger.info("Requesting data to a table\n"
                    "Process: {}\n"
                    "Length: {}\n"
                    "Start: {}\n"
                    "Ordered by: {}\n"
                    "Ordered in: {}\n"
                    "Pesquisar por:{}\n".format(self.get_view_details(), self.length, self.start, self.order_column,
                                                self.order_direction, self.global_search))

    def get_ajax_url(self):
        return ""

    def get_id_prefix(self):
        return ""

    @abstractmethod
    def get_view_details(self):
        pass

    def has_click_option(self):
        return self.on_click_url != "#"

    def set_menu_length(self):
        return [[10, 20, 40], [10, 20, 40]]

    def set_page_length(self):
        return 10

    def set_order(self):
        return [[1, 'asc']]

    def template(self):
        self.pre_config()
        self.queryset = self.set_query_set()
        self.object_list = self.produce_query_set()
        self.object_list = self.post_config()
        self.set_number()
        self.object_list = self.to_table_topics()

        return self.get_objects()

    @abstractmethod
    def set_thead(self):
        pass

    @abstractmethod
    def set_searchable(self):
        pass

    def set_number(self):
        self.number = self.queryset.count()

    def pre_config(self):
        self.order_column -= 1
        self.order_attr = self.thead[self.order_column][0]
        self.is_reverse = True if self.order_direction == '-' else False

    def post_config(self):
        paginator = Paginator(self.object_list, self.length)  # items per page
        page = paginator.page(
            int(((self.start + self.length / 2) / self.length)) + 1)
        return page.object_list

    def produce_query_set(self):
        qs = Q()
        if len(self.global_search):
            queries = [Q(**{f[0]: self.global_search})
                       for f in self.searchable_fields]
            for query in queries:
                qs = qs | query
        self.queryset = self.queryset.filter(qs).order_by(
            self.order_direction + self.thead[self.order_column][0])
        return self.queryset

    @abstractmethod
    def set_query_set(self):
        pass

    def to_table_topics(self):
        obj_set = []
        for item in self.object_list:
            data = dict()
            if self.request.GET.get("selectable", False):
                data["selectable"] = ""
            data["redirect_link"] = self.resolve_redirect_link(item)
            data["DT_RowId"] = self.add_row_id(item)
            for field in self.thead:
                field_name = field[0]
                try:
                    if "__" in field_name:
                        values = field_name.split("__")
                        temp = item
                        size = len(values)
                        instance = None
                        for i in range(size):
                            if i == (size - 1):
                                instance = temp
                                field = values[i]
                            else:
                                temp = getattr(temp, values[i])
                        value = self.resolve_best_value(instance, field)
                    else:
                        value = self.resolve_best_value(item, field_name)
                    data[field_name] = value
                except:
                    data[field_name] = "Error"
                    logger.exception("Error")
            obj_set.append(OrderObject(data, self.order_attr))
        return obj_set

    def resolve_best_value(self, instance, field):
        try:
            return getattr(instance, "get_{}_display".format(field))()
        except:
            value = getattr(instance, field, None)
            if isinstance(value, datetime):
                return formats.date_format(value, 'SHORT_DATETIME_FORMAT')
            elif isinstance(value, bool):
                return value
            elif issubclass(type(value), PolymorphicModel):
                return str(type(value).objects.get(pk=value.pk))
            elif value is None:
                return None
            else:
                temp = str(value)
                if len(temp) > 80:
                    return temp[:80]+"..."
                else:
                    return temp

    def resolve_redirect_link(self, instance):
        if self.on_click_url != "#":
            keys = self.extra_params.keys()
            if len(keys) > 0:
                kwargs = self.extra_params.get("kwargs", None)
                args = self.extra_params.get("args", None)

                resolved_kwargs = {}
                resolved_args = ()

                for key, element in kwargs.items():
                    if "__" in element:
                        splited_attrs = element.split("__")
                        temp = None
                        for attr in splited_attrs:
                            temp = getattr(instance, attr, None)
                        resolved_kwargs[key] = temp
                    else:
                        resolved_kwargs[key] = getattr(instance, element, None)

                if args is not None:
                    for element in args:
                        resolved_args += (getattr(instance, element, None))

                return reverse(self.on_click_url, kwargs=resolved_kwargs, args=resolved_args)
            else:
                return reverse(self.on_click_url)
        else:
            return "#"

    def add_row_id(self, item):
        return self.id_prefix + str(getattr(item, "pk"))

    def get_objects(self):
        if self.request.is_ajax():
            result = []
            for instance in self.object_list:
                json_order = vars(instance)
                # del json_order["order_key"]
                result.append(json_order)
            return JsonResponse({
                "draw": self.draw,
                "recordsTotal": self.queryset.count(),
                "recordsFiltered": self.number,
                "data": result,
            })
        return self.object_list

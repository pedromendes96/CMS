from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from wagtail.contrib.modeladmin.views import IndexView
from .tables.process import Process

# Create your views here.


class AjaxView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class TableIndexView(IndexView):
    process_class = None

    def dispatch(self, request, *args, **kwargs):
        self.process = self.process_class(
            request, **self.get_extra_context_table())
        if request.is_ajax():
            return getattr(self, request.method.lower())(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.process.template()
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            "process": self.process
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def get_extra_context_table(self):
        return {}

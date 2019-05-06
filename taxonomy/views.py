from django.shortcuts import render
from wagtail.contrib.modeladmin.views import IndexView
from .models import Section, Category
# Create your views here.


class SectionIndexView(IndexView):
    def get_context_data(self, **kwargs):
        sections = self.get_base_queryset()
        all_data = []
        for section in sections:
            section_data = dict()
            section_data["instance"] = section
            section_data["children"] = section.get_categories_hierarchy()
            all_data.append(section_data)

        context = {
            "data": all_data,
            "category_name": Category.__name__,
            "section_name": Section.__name__
        }
        context.update(kwargs)
        return super().get_context_data(**context)

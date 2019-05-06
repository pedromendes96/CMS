from django.conf.urls import include, url
from django.urls import path
from . import api_views

urlpatterns = [
    path("get/schema/", api_views.GetTaxonomySchema.as_view(),
         name="get_taxonomy_schema")
]

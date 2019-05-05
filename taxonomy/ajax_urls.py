from django.conf.urls import include, url
from .ajax_views import OnInactivate, OnCreate, OnRename, AjaxTreeStructure, OnActivate, OnMove


urlpatterns = [
    url(r'^rootTreeCall/$', AjaxTreeStructure.as_view(),
        name="ajax_tree_structure"),
    url(r'^OnMove/$', OnMove.as_view(),
        name="ajax_move"),
    url(r'^inactivate/$', OnInactivate.as_view(),
        name="ajax_inactivate"),
    url(r'^activate/$', OnActivate.as_view(),
        name="ajax_activate"),
    url(r'^create/$', OnCreate.as_view(),
        name="ajax_create"),
    url(r'^rename/$', OnRename.as_view(),
        name="ajax_rename"),
]

from django.conf.urls import include, url

urlpatterns = [
    url(r'^taxonomy/', include("taxonomy.ajax_urls"))
]

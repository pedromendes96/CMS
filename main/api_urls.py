from django.conf.urls import include, url
from django.urls import path
from comments.api_urls import

urlpatterns = [
    path('casserver-notification/',
         views.CASNotification.as_view(), name='notification'),
]

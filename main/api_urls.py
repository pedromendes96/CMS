from django.conf.urls import include, url
from django.urls import path
from . import views
from client.views import CASNotification
from comments.api_urls import urlpatterns as comments_api_urls
from sports.api_urls import urlpatterns as sports_api_urls
from news.api_urls import urlpatterns as news_api_urls
from taxonomy.api_urls import urlpatterns as taxonomy_api_urls
from cases_of_the_day.api_urls import urlpatterns as cases_of_the_day_api_urls

urlpatterns = [
    path('casserver-notification/', CASNotification.as_view(), name='notification'),
    path('comments/', include(comments_api_urls)),
    path('sports/', include(sports_api_urls)),
    path('news/', include(news_api_urls)),
    path('taxonomy/', include(taxonomy_api_urls)),
    path('cases_of_the_day/', include(cases_of_the_day_api_urls))
]

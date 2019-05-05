from django.urls import path
from .views import CustomClickTrackingView, CustomOpenTrackingView

urlpatterns = [
    path(
        "open/<str:path>/", CustomOpenTrackingView.as_view(), name="open_tracking"),
    path(
        "click/<str:path>/", CustomClickTrackingView.as_view(), name="click_tracking"),
]

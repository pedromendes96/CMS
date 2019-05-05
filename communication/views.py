from django.shortcuts import render
from pytracking.django import OpenTrackingView, ClickTrackingView

import logging

logger = logging.getLogger("communication")
# Create your views here.


class CustomOpenTrackingView(OpenTrackingView):
    def notify_tracking_event(self, tracking_result):
        # Override this method to do something with the tracking result.
        # tracking_result.request_data["user_agent"] and
        # tracking_result.request_data["user_ip"] contains the user agent
        # and ip of the client.
        send_tracking_result_to_queue(tracking_result)

    def notify_decoding_error(self, exception):
        # Called when the tracking link cannot be decoded
        # Override this to, for example, log the exception
        logger.exception(exception)


class CustomClickTrackingView(ClickTrackingView):
    def notify_tracking_event(self, tracking_result):
        # Override this method to do something with the tracking result.
        # tracking_result.request_data["user_agent"] and
        # tracking_result.request_data["user_ip"] contains the user agent
        # and ip of the client.
        send_tracking_result_to_queue(tracking_result)

    def notify_decoding_error(self, exception):
        # Called when the tracking link cannot be decoded
        # Override this to, for example, log the exception
        logger.log(exception)
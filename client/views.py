from urllib.parse import urljoin

import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.utils.translation import gettext as _
from django.utils import timezone
from .sessions import SessionStore as Session
from rest_framework.views import APIView
from django.db import DatabaseError, transaction

from .utils import get_cas_token


class CASNotification(APIView):
    def post(self, request, *args, **kwargs):
        data = self._request_session_info_CAS(request)
        self._force_update_session_user(data)
        return HttpResponse({})

    def _force_update_session_user(self, data):
        for session in data:
            session_key = session['session_key']
            Session(session_key=session_key).load()

    def _request_session_info_CAS(self, request):
        callback = request.POST.get('callback', None)

        url = urljoin(settings.DCS_API_ENDPOINT, callback)
        timeout = settings.DCS_API_TIMEOUT
        rs = requests.get(url, timeout=timeout, allow_redirects=False)
        return rs.json()

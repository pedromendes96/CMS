import json
import logging

import urllib3

from .utils import get_cas_token
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, HASH_SESSION_KEY
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.sessions.backends.cache import SessionStore as CacheSessionStore

logger = logging.getLogger('polls')

UserModel = get_user_model()
KEY_PREFIX = ""


class SessionStore(CacheSessionStore):
    """
    A cache-based session store.
    """

    def load(self):

        try:
            session_data = self._cache.get(self.cache_key)
        except Exception:
            logger.exception(
                "couldnt get the session with the key -> {}".format(self.cache_key))
            # Some backends (e.g. memcache) raise an exception on invalid
            # cache keys. If this happens, reset the session. See #17810.
            session_data = None

        if session_data is not None:
            return session_data

        try:
            http = urllib3.PoolManager()
            token = get_cas_token()
            if token is None:
                raise Exception("There is no token in the DB")
            headers = {'Authorization': 'Token {}'.format(token)}
            response = http.request('POST', settings.DCAS_SESSION_ENDPOINT, headers=headers,
                                    fields={settings.SESSION_COOKIE_NAME: self._session_key})
            if response.status == 200:
                result = json.loads(response.data.decode('utf-8'))
                json_res = result["session"]
                json_groups = result["groups"]
                try:
                    user = UserModel.objects.get(
                        id=int(json_res["user"]["id"]))
                    self._update_groups(json_groups, user)
                except Exception as identifier:
                    logger.exception(
                        "This means that process of update groups cant be done now because the respective user still didnt go to one page of this service after being authenticated in one service.")
                if 'session' in json_res and BACKEND_SESSION_KEY in json_res['session'] and HASH_SESSION_KEY in json_res['session']:
                    session_dict = json_res['session']
                    session_dict[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
                    session_dict[HASH_SESSION_KEY] = True
                    session_dict['user_roles'] = json_res['user_roles']
                    session_dict['user'] = json_res['user']
                    session_dict["groups"] = json_groups
                    # @check
                    session_dict['history_roles'] = json_res['history_roles']
                    session_dict['warnings'] = json_res['warnings']
                    session_dict["consumables"] = json_res['consumables']
                    self._cache.set(key=self.cache_key, value=session_dict,
                                    timeout=settings.DCAS_SESSION_CACHE_TIMEOUT)
                    return session_dict

            # print(vars(response))
            # return session_data
        except Exception:
            logger.exception("SessionStore.load -> Some error in request")
            session_data = None

        self._session_key = None
        return {}

    def _update_groups(self, json_groups, user):
        valid_groups_names = []
        for group in json_groups:
            valid_groups_names.append(group["name"])
        groups_user = user.groups.all()
        for group in groups_user:
            if group.name not in valid_groups_names:
                group.delete()

        for group in valid_groups_names:
            try:
                group = Group.objects.get(name=group)
            except Exception as identifier:
                group = Group.objects.create(name=group)
            if group not in groups_user:
                user.groups.add(group)

"""DCAS authentication backend"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django_cas_ng.backends import CASBackend
from django.conf import settings
import requests
import json


__all__ = ['DCASBackend']


class DCASBackend(CASBackend):
    """CAS authentication backend"""

    def authenticate(self, request, ticket, service):
        """Verifies CAS ticket and gets or creates User object"""
        user = super(DCASBackend, self).authenticate(
            request=request, ticket=ticket, service=service)
        user.pk = get_user_model()._meta.pk.to_python(user.pk)
        json_groups = request.session["groups"]
        self._update_groups(json_groups, user)
        return user

    def get_user_id(self, attributes):
        """ just to fix it, it should be and integer """
        user_id = super(DCASBackend, self).get_user_id(attributes=attributes)
        return get_user_model()._meta.pk.to_python(user_id)

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

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from utils.models import ActivatableModel
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.


class RemoteUser(AbstractUser):

    def get_session_auth_hash(self):
        # """
        # Return an HMAC of the password field.
        # """
        # key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        # return salted_hmac(key_salt, self.password).hexdigest()
        return True

    @property
    def is_admin(self):
        group = Group.objects.get(name="Administration")
        return group in self.groups.all()

    class Meta:
        verbose_name = _('Remote User')
        verbose_name_plural = _('Remote Users')


class ServiceInfo(ActivatableModel):
    """
    it will save in the db the services registered in the mediator
    """
    is_cas = models.BooleanField(verbose_name=_("Is CAS"), default=False)
    name = models.CharField(verbose_name=_("Service model"), max_length=64)
    token = models.CharField(verbose_name=_("Service Token"), max_length=512)
    base_url = models.URLField(verbose_name=_("Base url"))
    domain = models.CharField(verbose_name=_("Domain"), max_length=512)

    def add_authorization(self, context):
        context.update({
            "Authorization": "Token {}".format(self.token)
        })

    panels = [
        FieldPanel('name'),
        FieldPanel('base_url'),
        FieldPanel('is_cas'),
        FieldPanel('domain'),
        FieldPanel('token'),
        FieldPanel('active'),
    ]

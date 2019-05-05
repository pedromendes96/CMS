from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


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

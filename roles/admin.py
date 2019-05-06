from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import Role, ServiceRole
from client.models import ServiceInfo
from django.apps import apps

# Register your models here.
app = apps.get_app_config('roles')
for model_name, model in app.models.items():
    admin.site.register(model)


class ServicesAdmin(ModelAdmin):
    model = ServiceInfo
    menu_label = 'Service'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-server'  # change as required
    list_display = ('identifier', 'name')
    list_filter = ('identifier', 'name')
    search_fields = ('identifier', 'name')


class RolesAdmin(ModelAdmin):
    model = Role
    menu_label = 'Role'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-user-secret'  # change as required
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class ServiceRolesAdmin(ModelAdmin):
    model = ServiceRole
    menu_label = 'ServiceRole'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-user-secret'  # change as required
    list_display = ('external_identifier',)
    list_filter = ('external_identifier',)
    search_fields = ('external_identifier',)


class AccessRestrictionGroup(ModelAdminGroup):
    menu_label = 'Restriction'
    menu_icon = 'fa-plug'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ServicesAdmin, RolesAdmin, ServiceRolesAdmin)


modeladmin_register(AccessRestrictionGroup)

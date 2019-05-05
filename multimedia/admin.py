from django.contrib import admin
from django.apps import apps
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import FacebookPage, FacebookGroup, FacebookStream, FacebookStreamRelation

# Register your models here.
app = apps.get_app_config('multimedia')
for model_name, model in app.models.items():
    admin.site.register(model)


class FacebookStreamModelAdmin(ModelAdmin):
    model = FacebookStream
    menu_label = 'Facebook Stream'  # ditch this to use verbose_name_plural from model
    menu_icon = 'media'  # change as required
    list_display = ('description', 'is_live', 'is_scheduled',
                    'show_in_home_page', 'title', 'short_description')
    list_filter = ('description', 'is_live', 'is_scheduled',
                   'show_in_home_page', 'title', 'short_description')
    search_fields = ('description', 'is_live', 'is_scheduled',
                     'show_in_home_page', 'title', 'short_description')


class FacebookPageModelAdmin(ModelAdmin):
    model = FacebookPage
    menu_label = 'Facebook Page'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-file'  # change as required
    list_display = ('name', 'access_token', 'facebook_id')
    list_filter = ('name', 'access_token', 'facebook_id')
    search_fields = ('name', 'access_token', 'facebook_id')


class FacebookGroupModelAdmin(ModelAdmin):
    model = FacebookGroup
    menu_label = 'Facebook Group'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('name', 'access_token', 'facebook_id')
    list_filter = ('name', 'access_token', 'facebook_id')
    search_fields = ('name', 'access_token', 'facebook_id')


class StreamModelAdminGroup(ModelAdminGroup):
    menu_label = 'Streaming'
    menu_icon = 'media'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (FacebookPageModelAdmin, FacebookGroupModelAdmin,
             FacebookStreamModelAdmin)


modeladmin_register(StreamModelAdminGroup)

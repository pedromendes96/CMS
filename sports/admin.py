from django.contrib import admin
from django.apps import apps
from django.utils.translation import gettext as _
from . import models
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)

# Register your models here.
app = apps.get_app_config('sports')
for model_name, model in app.models.items():
    admin.site.register(model)


class SoccerCompetitionModelAdmin(ModelAdmin):
    model = models.SoccerCompetition
    # ditch this to use verbose_name_plural from model
    menu_label = _('Soccer Competetion')
    menu_icon = 'media'  # change as required
    list_display = ()
    list_filter = ()
    search_fields = ()


class SoccerMatchModelAdmin(ModelAdmin):
    model = models.SoccerMatch
    # ditch this to use verbose_name_plural from model
    menu_label = _('Soccer Match')
    menu_icon = 'fa-file'  # change as required
    list_display = ()
    list_filter = ()
    search_fields = ()


class SoccerTeamModelAdmin(ModelAdmin):
    model = models.SoccerTeam
    # ditch this to use verbose_name_plural from model
    menu_label = _('Soccer Team')
    menu_icon = 'fa-users'  # change as required
    list_display = ()
    list_filter = ()
    search_fields = ()


class SoccerVideoModelAdmin(ModelAdmin):
    model = models.SoccerVideo
    # ditch this to use verbose_name_plural from model
    menu_label = _('Soccer Video')
    menu_icon = 'fa-users'  # change as required
    list_display = ()
    list_filter = ()
    search_fields = ()


class SportsAdminGroup(ModelAdminGroup):
    menu_label = _('Sports')
    menu_icon = 'fa-soccer-ball-o'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (SoccerCompetitionModelAdmin, SoccerMatchModelAdmin,
             SoccerTeamModelAdmin, SoccerVideoModelAdmin)


modeladmin_register(SportsAdminGroup)

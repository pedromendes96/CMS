from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import CasesOfTheDay, Region, Locals
from django.apps import apps

# Register your models here.
app = apps.get_app_config('cases_of_the_day')
for model_name, model in app.models.items():
    admin.site.register(model)


# Wagtail administration


class CasesOfTheDayAdmin(ModelAdmin):
    model = CasesOfTheDay
    menu_label = 'Cases of the day'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show people managed by the current user
        return qs.order_by("-updated_at")


class RegionAdmin(ModelAdmin):
    model = Region
    menu_label = 'Region'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-map-pin'  # change as required
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class LocalsAdmin(ModelAdmin):
    model = Locals
    menu_label = 'Location'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-map-marker'  # change as required
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class LocalizationGroup(ModelAdminGroup):
    menu_label = 'Localizations'
    menu_icon = 'fa-compass'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (RegionAdmin, LocalsAdmin)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(LocalizationGroup)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(CasesOfTheDayAdmin)

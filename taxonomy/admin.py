from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Section, Category
from .views import SectionIndexView
from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from django.apps import apps

# Register your models here.
app = apps.get_app_config('taxonomy')
for model_name, model in app.models.items():
    admin.site.register(model)


class TaxonomyModelAdmin(ModelAdmin):
    model = Section
    index_view_class = SectionIndexView
    menu_label = _('Taxonomy')
    menu_icon = 'fa-sitemap'  # change as required
    menu_order = None  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False


class SectionModelAdmin(ModelAdmin):
    model = Section
    menu_label = _('Section')
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ('name', 'img')
    list_filter = ('name',)
    search_fields = ('name', 'description')


class CategoryModelAdmin(ModelAdmin):
    model = Category
    menu_label = _('Category')
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ('name', 'img')
    list_filter = ('name',)
    search_fields = ('name', 'description')


modeladmin_register(TaxonomyModelAdmin)
modeladmin_register(CategoryModelAdmin)
modeladmin_register(SectionModelAdmin)

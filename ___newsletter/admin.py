from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Newsletter
from django.apps import apps

# Register your models here.
app = apps.get_app_config('newsletter')
for model_name, model in app.models.items():
    admin.site.register(model)


class NewslettersAdmin(ModelAdmin):
    model = Newsletter
    menu_label = 'Newsletter'  # ditch this to use verbose_name_plural from model
    menu_icon = 'mail'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show people managed by the current user
        return qs.order_by("-updated_date")


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(NewslettersAdmin)

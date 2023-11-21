from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import Lullaby, Region


@admin.register(Lullaby)
class LullabyAdmin(TranslationAdmin):
    list_display = ["pk", "name", "region", "get_type", "source", "views"]

    def get_type(self, obj):
        return obj.get_type_display()

    get_type.short_description = _("type")


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ["pk", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }

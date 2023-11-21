from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Lullaby, Region


@admin.register(Lullaby)
class LullabyAdmin(TranslationAdmin):
    list_display = ["pk", "name", "region", "type", "source", "views"]


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ["pk", "name", "slug"]
    prepopulated_fields = {
        "slug": ["name"],
    }

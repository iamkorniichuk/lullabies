from django.contrib import admin

from .models import Lullaby, Region


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "region", "source", "views"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]

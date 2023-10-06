from django.contrib import admin

from .models import Lullaby


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "region", "source", "views"]

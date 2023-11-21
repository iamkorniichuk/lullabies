from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "sex"]

    def get_sex(self, obj):
        return obj.get_sex_display()

    get_sex.short_description = _("sex")

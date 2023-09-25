from django.contrib import admin
from django.utils.html import format_html

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ["pk", "url_name", "img_logo"]

    @admin.display(description="website")
    def url_name(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.website, obj.name)

    url_name.allow_tags = True

    @admin.display(description="logo")
    def img_logo(self, obj):
        return format_html('<img src="{}">', obj.logo)

    img_logo.allow_tags = True

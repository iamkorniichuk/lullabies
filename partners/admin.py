from django.contrib import admin

from commons.admin import img_tag_factory, a_tag_factory

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "url_website", "img_logo", "img_logo_dark"]

    url_website = a_tag_factory("website", "website")
    img_logo = img_tag_factory("logo", "logo")
    img_logo_dark = img_tag_factory("logo dark theme", "logo_dark_theme")

from django.contrib import admin

from commons.admin import img_tag_factory, a_tag_factory

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "url_website", "img_classic_logo", "img_dark_logo"]

    url_website = a_tag_factory("website", "website")
    img_classic_logo = img_tag_factory("classic logo", "classic_logo")
    img_dark_logo = img_tag_factory("dark logo", "dark_logo")

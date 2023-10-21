from django.contrib import admin

from commons.admin import a_file_tag_factory

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["pk", "url_file"]

    url_file = a_file_tag_factory("file", "file")

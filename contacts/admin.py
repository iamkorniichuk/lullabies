from modeltranslation.admin import TranslationAdmin
from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ["id", "name", "value"]

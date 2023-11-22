from django import forms
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from django_svg_image_form_field import SvgAndImageFormField
from commons.admin import img_tag_factory, a_tag_factory

from .models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        exclude = []
        field_classes = {
            "classic_logo": SvgAndImageFormField,
            "dark_logo": SvgAndImageFormField,
        }


@admin.register(Partner)
class PartnerAdmin(TranslationAdmin):
    list_display = ["pk", "name", "url_website", "img_classic_logo", "img_dark_logo"]
    form = PartnerForm

    url_website = a_tag_factory("website", "website")
    img_classic_logo = img_tag_factory("classic logo", "classic_logo")
    img_dark_logo = img_tag_factory("dark logo", "dark_logo")

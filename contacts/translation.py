from modeltranslation.translator import register, TranslationOptions

from .models import Contact


@register(Contact)
class ContactTranslation(TranslationOptions):
    fields = ["value"]
    required_languages = {"default": ["value"]}

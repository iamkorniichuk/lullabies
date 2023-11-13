from django.conf import settings

from modeltranslation.translator import translator
from transliterate import translit
from transliterate.exceptions import LanguagePackNotFound


class AutoTransliterationMixin:
    def save(self, *args, **kwargs):
        default_language = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        options = translator.get_options_for_model(type(self))
        for name, fields in options.local_fields.items():
            original_value = getattr(self, f"{name}_{default_language}")
            if default_language != "en":
                original_value = translit(
                    original_value, default_language, reversed=True
                )
            for translation_field in fields:
                language = translation_field.language
                if default_language == language:
                    continue
                try:
                    transliterated_text = translit(original_value, language)
                    setattr(self, translation_field.name, transliterated_text)
                except LanguagePackNotFound:
                    setattr(self, translation_field.name, original_value)
        return super().save(*args, **kwargs)

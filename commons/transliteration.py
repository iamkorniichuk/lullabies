from django.conf import settings
from django.utils.translation import get_language

from transliterate import translit
from transliterate.exceptions import LanguagePackNotFound

from rest_framework.serializers import ReadOnlyField

DEFAULT_LANGUAGE = settings.MODELTRANSLATION_DEFAULT_LANGUAGE


def get_translit(value, lang):
    if DEFAULT_LANGUAGE != "en":
        value = translit(
            value,
            DEFAULT_LANGUAGE,
            reversed=True,
        )
    try:
        return translit(value, lang)
    except LanguagePackNotFound:
        return value


def get_translit_property(field, lang):
    return property(lambda self: get_translit(getattr(self, field), lang))


def register_transliteration(model, fields):
    model.translit_fields = fields
    translit_fields = get_translit_fields(fields)
    for field, translit_fields in translit_fields.items():
        for name, lang in translit_fields:
            setattr(
                model,
                name,
                get_translit_property(f"{field}_{DEFAULT_LANGUAGE}", lang),
            )


class TransliterationSerializerMixin:
    def __init__(self, *args, **kwargs):
        current_language = get_language()
        for field, translit_fields in get_translit_fields(
            self.Meta.model.translit_fields
        ).items():
            for name, lang in translit_fields:
                if lang == current_language:
                    self.fields[f"{field}_translit"] = ReadOnlyField(source=name)
        super().__init__(*args, **kwargs)


def get_translit_fields(fields):
    result = {}
    for field in fields:
        result[field] = []
        for code, _ in settings.LANGUAGES:
            if code == settings.MODELTRANSLATION_DEFAULT_LANGUAGE:
                continue
            result[field].append((f"{field}_translit_{code}", code))
    return result

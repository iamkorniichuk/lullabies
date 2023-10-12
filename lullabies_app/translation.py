from modeltranslation.translator import register, TranslationOptions

from .models import Lullaby, Region


@register(Lullaby)
class LullabyTranslation(TranslationOptions):
    fields = ["name", "lyrics"]
    required_languages = {"default": ["name"]}


@register(Region)
class RegionTranslation(TranslationOptions):
    fields = ["name"]
    required_languages = {"default": fields}

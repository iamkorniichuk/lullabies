from modeltranslation.translator import register, TranslationOptions

from .models import Lullaby


@register(Lullaby)
class LullabyTranslation(TranslationOptions):
    fields = ["name", "lyrics"]
    required_languages = {"default": fields}

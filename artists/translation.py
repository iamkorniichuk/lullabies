from modeltranslation.translator import register, TranslationOptions

from .models import Artist


@register(Artist)
class ArtistTranslation(TranslationOptions):
    fields = ["name"]
    required_languages = {"default": fields}

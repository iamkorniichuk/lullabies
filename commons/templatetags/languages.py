from django import template
from django.conf import settings

register = template.Library()


@register.filter
def switch_lang(request, language):
    lang_codes = [c for (c, name) in settings.LANGUAGES]

    parts = request.get_full_path().split("/")

    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = "/" + language

    return "/".join(parts)

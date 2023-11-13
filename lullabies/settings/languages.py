LANGUAGE_CODE = "uk"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = [
    ("uk", gettext("Ukraine")),
    ("en", gettext("English")),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = "uk"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

gettext = lambda s: s
LANGUAGES = [
    ("en", gettext("English")),
    ("uk", gettext("Ukraine")),
]

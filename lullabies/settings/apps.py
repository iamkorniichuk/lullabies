CONTRIB_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CREATED_APPS = [
    "commons",
    "artists",
    "contacts",
    "documents",
    "emails",
    "lullabies_app",
    "media",
    "partners",
    "statistic",
]

IMPORTED_APPS = [
    "rest_framework",
    "storages",
    "corsheaders",
    "drf_yasg",
    "django_ses",
    "django_cleanup.apps.CleanupConfig",
    "django_filters",
]

INSTALLED_APPS = (
    [
        "modeltranslation",
    ]
    + CONTRIB_APPS
    + IMPORTED_APPS
    + CREATED_APPS
)

from .env import env
import json


def json_loads_or_none(value):
    if value is None:
        return None
    return json.loads(value)


SECRET_KEY = env("SECRET_KEY")

DEBUG = env("IS_DEVELOPMENT", cast=bool, default=True)

ALLOWED_HOSTS = env("APP_HOSTS", cast=json_loads_or_none, default=["localhost"])

ROOT_URLCONF = "lullabies.urls"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

WSGI_APPLICATION = "lullabies.wsgi.application"

cors_origins = env("CORS_ORIGINS", cast=json_loads_or_none)
if cors_origins:
    CORS_ALLOWED_ORIGINS = cors_origins
else:
    CORS_ALLOW_ALL_ORIGINS = True

from .env import env
from environ import NoValue
import json


def get_json_env(name, default=None):
    try:
        value = env(name, default=NoValue())
        if isinstance(value, NoValue):
            return default
        return json.loads(env(name))
    except json.JSONDecodeError:
        return default


SECRET_KEY = env("SECRET_KEY")

DEBUG = env("IS_DEVELOPMENT", cast=bool, default=True)

ALLOWED_HOSTS = get_json_env("APP_HOSTS", default=["localhost"])

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

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
cors_origins = get_json_env("CORS_ORIGINS")
if cors_origins:
    CORS_ALLOWED_ORIGINS = cors_origins
else:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = False

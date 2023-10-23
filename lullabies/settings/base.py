from .env import env

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("IS_DEVELOPMENT", cast=bool, default=True)

ALLOWED_HOSTS = [
    env("APP_HOST", default="localhost"),
]

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


CORS_ALLOW_ALL_ORIGINS = True

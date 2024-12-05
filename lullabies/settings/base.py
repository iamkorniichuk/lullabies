from .env import env


SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("IS_DEVELOPMENT", default=True)

ALLOWED_HOSTS = env.list("APP_HOSTS")

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
cors_origins = env.list("CORS_ORIGINS", default=[])
if cors_origins:
    CORS_ALLOWED_ORIGINS = cors_origins
else:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = False

ADMIN_TWO_FACTOR_NAME = "kolyskova"

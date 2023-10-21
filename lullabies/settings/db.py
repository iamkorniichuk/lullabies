from .env import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("RDS_DB_NAME"),
        "USER": env("RDS_USERNAME"),
        "PASSWORD": env("RDS_PASSWORD"),
        "HOST": env("RDS_HOSTNAME"),
        "PORT": env("RDS_PORT"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

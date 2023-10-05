from django.apps import AppConfig
from django.db.models.signals import pre_save


class MediaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "media"

    def ready(self):
        from .models import MediaSource
        from .signals import update_duration

        pre_save.connect(update_duration, MediaSource)

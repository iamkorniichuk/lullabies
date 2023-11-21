from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _


class MediaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "media"
    verbose_name = _("media")

    def ready(self):
        from .models import MediaSource
        from .signals import update_duration

        pre_save.connect(update_duration, MediaSource)

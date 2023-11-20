from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LullabiesAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lullabies_app"
    verbose_name = _("lullabies")

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .lullaby import Lullaby


def today_date():
    return timezone.now()


class Boost(models.Model):
    class Meta:
        verbose_name = _("boost")
        verbose_name_plural = _("boosts")

    lullabies = models.ManyToManyField(
        Lullaby,
        related_name="boosts",
        verbose_name=_("lullabies"),
    )
    date = models.DateField(unique=True, default=today_date)

    def __repr__(self):
        return f"Boost({self.date})"

    def __str__(self):
        return f"{self.date}"

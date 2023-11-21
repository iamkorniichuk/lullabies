from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.transliteration import register_transliteration


class SexChoices(models.TextChoices):
    MALE = "M", _("male")
    FEMALE = "F", _("female")
    UNDEFINED = "U", _("undefined")


class Artist(models.Model):
    class Meta:
        verbose_name = _("artist")
        verbose_name_plural = _("artists")

    name = models.CharField(max_length=128, verbose_name=_("name"))
    sex = models.CharField(
        max_length=16,
        choices=SexChoices.choices,
        verbose_name=_("sex"),
    )

    def __repr__(self):
        return f"Artist({self.name})"

    def __str__(self):
        return self.name


register_transliteration(Artist, ["name"])

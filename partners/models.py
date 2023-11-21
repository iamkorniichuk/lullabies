from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    class Meta:
        verbose_name = _("partner")
        verbose_name_plural = _("partners")

    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    classic_logo = models.ImageField(
        upload_to="logo/classic", verbose_name=_("classic logo")
    )
    dark_logo = models.ImageField(upload_to="logo/dark", verbose_name=_("dark logo"))
    website = models.URLField(unique=True, verbose_name=_("website"))

    def get_absolute_url(self):
        return reverse("partner-detail", kwargs={"pk": self.pk})

    def __repr__(self):
        return f"Partner({self.name})"

    def __str__(self):
        return self.name

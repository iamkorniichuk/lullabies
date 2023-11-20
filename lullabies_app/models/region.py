from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    class Meta:
        verbose_name = _("region")
        verbose_name_plural = _("regions")

    name = models.CharField(max_length=128, verbose_name=_("name"))
    slug = models.SlugField(
        max_length=128,
        unique=True,
        blank=True,
        verbose_name=_("slug"),
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Region({self.name})"

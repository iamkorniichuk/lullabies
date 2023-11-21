from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    name = models.SlugField(max_length=64, verbose_name=_("name"))
    value = models.CharField(max_length=312, verbose_name=_("value"))

    def __repr__(self):
        return f"Contact({self.name})"

    def __str__(self):
        return self.name

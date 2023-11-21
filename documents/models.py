from django.db import models
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")

    name = models.CharField(max_length=48, verbose_name=_("name"))
    file = models.FileField(upload_to="documents", verbose_name=_("file"))

    def __str__(self):
        return f"Document({self.name})"

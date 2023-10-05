from django.db import models
from django.urls import reverse

from artists.models import Artist

from media.models import MediaSource
from .region import RegionChoices


class Lullaby(models.Model):
    class Meta:
        verbose_name_plural = "lullabies"

    name = models.CharField(max_length=64)
    region = models.CharField(max_length=64, choices=RegionChoices.choices)
    lyrics = models.TextField()
    artists = models.ManyToManyField(
        Artist,
        related_name="lullabies",
        blank=True,
    )
    source = models.OneToOneField(
        MediaSource,
        models.RESTRICT,
        related_name="lullaby",
    )

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"

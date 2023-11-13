from django.db import models
from django.urls import reverse
from django.conf import settings

from artists.models import Artist
from media.models import MediaSource
from commons.transliteration import AutoTransliterationMixin

from .region import Region


class Lullaby(AutoTransliterationMixin, models.Model):
    class Meta:
        verbose_name_plural = "lullabies"
        constraints = [
            models.CheckConstraint(
                check=models.Q(region__isnull=True) ^ models.Q(artist__isnull=True),
                name="only_region_or_artist_is_set",
                violation_error_message="You need to specify only region or artist.",
            ),
        ]

    name = models.CharField(max_length=64)
    region = models.ForeignKey(
        Region,
        models.SET_NULL,
        related_name="lullabies",
        null=True,
        blank=True,
    )
    artist = models.ForeignKey(
        Artist,
        models.SET_NULL,
        related_name="lullabies",
        null=True,
        blank=True,
    )
    lyrics = models.TextField(blank=True, default="")
    source = models.OneToOneField(
        MediaSource,
        models.RESTRICT,
        related_name="lullaby",
    )
    views = models.PositiveIntegerField(
        default=0,
        editable=False,
    )

    def save(self, *args, **kwargs):
        default_language = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        field_name = f"lyrics_{default_language}"
        original_lyrics = getattr(self, field_name).split("\n")
        lyrics = []
        for i, line in enumerate(original_lyrics):
            if line.isspace():
                i -= 1
                continue
            if i % 2 == 0 and i != 0:
                lyrics.append("\n")
            lyrics.append(line.strip())
        setattr(self, field_name, "\n".join(lyrics))

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"

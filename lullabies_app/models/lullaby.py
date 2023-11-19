from django.db import models
from django.urls import reverse
from django.conf import settings

from artists.models import Artist
from media.models import MediaSource
from commons.transliteration import register_transliteration

from .region import Region


class LullabyTypeChoices(models.TextChoices):
    NEW = "new", "new"
    ARCHIVE = "archive", "archive"


class Lullaby(models.Model):
    class Meta:
        verbose_name_plural = "lullabies"

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
    type = models.CharField(choices=LullabyTypeChoices.choices)

    def save(self, *args, **kwargs):
        field_name = f"lyrics_{settings.MODELTRANSLATION_DEFAULT_LANGUAGE}"
        lyrics = getattr(self, field_name)
        setattr(self, field_name, self.format_lyrics(lyrics))

        return super().save(*args, **kwargs)

    def format_lyrics(self, lyrics):
        original_lyrics = lyrics.split("\n")
        lyrics = []
        i = 0
        for line in original_lyrics:
            if line.isspace() or line == "":
                continue
            if i % 2 == 0 and i != 0:
                lyrics.append("\n")
            lyrics.append(line.strip())
            i += 1

        return "\n".join(lyrics)

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"


register_transliteration(Lullaby, ["name", "lyrics"])

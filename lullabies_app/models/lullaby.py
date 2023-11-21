from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from artists.models import Artist
from media.models import MediaSource
from commons.transliteration import register_transliteration

from .region import Region


class LullabyTypeChoices(models.TextChoices):
    NEW = "new", _("new")
    ARCHIVE = "archive", _("archive")


class Lullaby(models.Model):
    class Meta:
        verbose_name = _("lullaby")
        verbose_name_plural = _("lullabies")

    name = models.CharField(max_length=64, verbose_name=_("name"))
    region = models.ForeignKey(
        Region,
        models.SET_NULL,
        related_name="lullabies",
        null=True,
        blank=True,
        verbose_name=_("region"),
    )
    artist = models.ForeignKey(
        Artist,
        models.SET_NULL,
        related_name="lullabies",
        null=True,
        blank=True,
        verbose_name=_("artist"),
    )
    lyrics = models.TextField(blank=True, default="", verbose_name=_("lyrics"))
    source = models.OneToOneField(
        MediaSource, models.RESTRICT, related_name="lullaby", verbose_name=_("source")
    )
    views = models.PositiveIntegerField(
        default=0, editable=False, verbose_name=_("views")
    )
    type = models.CharField(choices=LullabyTypeChoices.choices, verbose_name=_("type"))

    def save(self, *args, **kwargs):
        field_name = f"lyrics_{settings.MODELTRANSLATION_DEFAULT_LANGUAGE}"
        lyrics = getattr(self, field_name)
        setattr(self, field_name, self.format_lyrics(lyrics))

        return super().save(*args, **kwargs)

    def format_lyrics(self, lyrics):
        original_lyrics = lyrics.split("\n")
        lyrics = []
        is_previous_line_space = False
        for line in original_lyrics:
            is_line_space = line.isspace() or line == ""
            if is_line_space:
                if is_previous_line_space:
                    continue
                lyrics.append("\n")
            else:
                lyrics.append(line.strip())
            is_previous_line_space = is_line_space

        return "\n".join(lyrics)

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __repr__(self):
        return f"Lullaby({self.name})"

    def __str__(self):
        return self.name


register_transliteration(Lullaby, ["name", "lyrics"])

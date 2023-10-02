from django.db import models
from django.urls import reverse

from artists.models import Artist

from .source import MediaSource
from .region import RegionChoices


class LullabyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class AudioLullabyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(source__format=models.Value("audio"))


class VideoLullabyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(source__format=models.Value("video"))


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
        related_name="lullabies",
    )

    objects = LullabyManager()
    audio_objects = AudioLullabyManager()
    video_objects = VideoLullabyManager()

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"

from django.db import models


class MediaSourceManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                format=models.ExpressionWrapper(
                    models.Case(
                        models.When(
                            ~models.Q(cover__exact="", audio__exact=""),
                            then=models.Value("audio"),
                        ),
                        models.When(
                            models.Q(video__isnull=False),
                            then=models.Value("video"),
                        ),
                        default=models.Value(""),
                    ),
                    output_field=models.CharField(),
                )
            )
        )


class MediaSource(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(video__isnull=False) ^ ~models.Q(audio__exact=""),
                name="only_one_source_is_set",
            ),
            models.CheckConstraint(
                check=models.Q(video__isnull=False)
                | models.Q(cover__exact="", audio__exact=""),
                name="audio_has_cover",
            ),
        ]

    video = models.URLField(blank=True, null=True)
    audio = models.FileField(blank=True, default="")
    cover = models.FileField(blank=True, default="")

    objects = MediaSourceManager()

    def __str__(self):
        return f"MediaSource({self.pk})"

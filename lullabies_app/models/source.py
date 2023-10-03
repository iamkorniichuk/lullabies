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
                check=models.Q(video__isnull=True) ^ models.Q(audio__exact=""),
                name="only_one_source_is_set",
                violation_error_message="You need to specify only one source of media: video or audio.",
            ),
            models.CheckConstraint(
                check=models.ExpressionWrapper(
                    models.Case(
                        models.When(
                            ~models.Q(audio__exact=""), then=~models.Q(cover__exact="")
                        ),
                        default=models.Value(True),
                    ),
                    output_field=models.BooleanField(),
                ),
                name="audio_has_cover",
                violation_error_message="If you use audio as a source, you need to upload a cover.",
            ),
        ]

    video = models.URLField(blank=True, null=True)
    audio = models.FileField(blank=True, default="", upload_to="audio/")
    cover = models.FileField(blank=True, default="", upload_to="cover/")

    objects = MediaSourceManager()

    def __str__(self):
        return f"MediaSource({self.pk})"

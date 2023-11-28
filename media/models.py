from django.db import models
from django.utils.translation import gettext_lazy as _


class MediaSourceManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                format=models.ExpressionWrapper(
                    models.Case(
                        models.When(
                            ~models.Q(audio__exact=""),
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
        verbose_name = _("media")
        verbose_name_plural = _("media")
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
                            models.Q(video__isnull=False),
                            then=~models.Q(preview__exact=""),
                        ),
                        default=models.Value(True),
                    ),
                    output_field=models.BooleanField(),
                ),
                name="video_has_preview",
                violation_error_message="If you use video as a source, you need to upload a preview.",
            ),
        ]

    video = models.URLField(blank=True, null=True, verbose_name=_("video"))
    audio = models.FileField(
        blank=True,
        default="",
        upload_to="audio/",
        verbose_name=_("audio"),
    )
    preview = models.ImageField(
        blank=True,
        default="",
        upload_to="preview/",
        verbose_name=_("preview"),
    )
    duration = models.DurationField(blank=True, null=True, verbose_name=_("duration"))
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)

    objects = MediaSourceManager()

    def __repr__(self):
        return f"Media({self.pk})"

    def __str__(self):
        return f"Media({self.pk}, {self.format})"

from django.contrib import admin

from commons.admin import img_tag_factory, a_tag_factory, a_file_tag_factory

from .models import MediaSource


@admin.register(MediaSource)
class MediaSource(admin.ModelAdmin):
    list_display = ["pk", "url_audio", "img_preview", "url_video", "format", "duration"]
    fieldsets = [
        [
            None,
            {
                "fields": ["audio", "preview", "video"],
            },
        ]
    ]

    img_preview = img_tag_factory("preview", "preview")
    url_audio = a_file_tag_factory("audio", "audio")
    url_video = a_tag_factory("audio", "video")

    @admin.display(description="format")
    def format(self, obj):
        return obj.format

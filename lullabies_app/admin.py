from django.contrib import admin
from django.utils.html import format_html


from .models import Lullaby, MediaSource


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "region", "source"]


@admin.register(MediaSource)
class MediaSource(admin.ModelAdmin):
    list_display = ["pk", "url_audio", "img_cover", "url_video", "format"]

    # TODO: Refactor
    @admin.display(description="cover")
    def img_cover(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" alt="{}" height="48">', obj.cover.url, obj.cover.name
            )

    img_cover.allow_tags = True

    @admin.display(description="audio")
    def url_audio(self, obj):
        if obj.audio:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', obj.audio.url, obj.audio.name
            )

    url_audio.allow_tags = True

    @admin.display(description="video")
    def url_video(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.video, obj.video)

    url_video.allow_tags = True

    @admin.display(description="format")
    def format(self, obj):
        return obj.format

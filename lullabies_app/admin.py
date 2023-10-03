from django.contrib import admin

from commons.admin import img_tag_factory, a_tag_factory, a_file_tag_factory

from .models import Lullaby, MediaSource


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "region", "source"]


@admin.register(MediaSource)
class MediaSource(admin.ModelAdmin):
    list_display = ["pk", "url_audio", "img_cover", "url_video", "format"]

    img_cover = img_tag_factory("cover", "cover")
    url_audio = a_file_tag_factory("audio", "audio")
    url_video = a_tag_factory("audio", "video")

    @admin.display(description="format")
    def format(self, obj):
        return obj.format

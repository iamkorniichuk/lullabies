from django.contrib import admin
from django.utils.html import format_html


from .models import Lullaby


@admin.register(Lullaby)
class LullabyAdmin(admin.ModelAdmin):
    list_display = ["pk", "url_name"]

    @admin.display(description="name")
    def url_name(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.name)

    url_name.allow_tags = True

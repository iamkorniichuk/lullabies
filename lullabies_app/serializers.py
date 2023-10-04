from rest_framework import serializers

from artists.serializers import ArtistSerializer

from .models import Lullaby, MediaSource


class MediaSource(serializers.ModelSerializer):
    class Meta:
        model = MediaSource
        fields = "__all__"

    format = serializers.SerializerMethodField("get_format")

    def get_format(self, obj):
        return obj.format


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = serializers.CharField(source="get_region_display")
    artists = ArtistSerializer(many=True)
    source = MediaSource()

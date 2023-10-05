from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from artists.serializers import ArtistSerializer

from .models import Lullaby, MediaSource


class MediaSource(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = MediaSource
        fields = "__all__"


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = serializers.CharField(source="get_region_display")
    artists = ArtistSerializer(many=True)
    source = MediaSource()

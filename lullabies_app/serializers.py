from rest_framework import serializers

from artists.serializers import ArtistSerializer
from media.serializers import MediaSourceSerializer

from .models import Lullaby, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["pk", "name"]


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = [
            "pk",
            "name",
            "region",
            "lyrics",
            "artists",
            "source",
            "views",
        ]

    region = RegionSerializer()
    artists = ArtistSerializer(many=True)
    source = MediaSourceSerializer()

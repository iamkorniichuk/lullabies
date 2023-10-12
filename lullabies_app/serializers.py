from rest_framework import serializers

from artists.serializers import ArtistSerializer
from media.serializers import MediaSourceSerializer

from .models import Lullaby, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = RegionSerializer()
    artists = ArtistSerializer(many=True)
    source = MediaSourceSerializer()

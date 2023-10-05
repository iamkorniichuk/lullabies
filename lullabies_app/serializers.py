from rest_framework import serializers

from artists.serializers import ArtistSerializer
from media.serializers import MediaSourceSerializer

from .models import Lullaby


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = serializers.CharField(source="get_region_display")
    artists = ArtistSerializer(many=True)
    source = MediaSourceSerializer()

from rest_framework import serializers

from artists.serializers import ArtistSerializer
from media.serializers import MediaSourceSerializer

from commons.transliteration import TransliterationSerializerMixin

from .models import Lullaby, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["pk", "name"]


class LullabySerializer(TransliterationSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = [
            "pk",
            "name",
            "region",
            "lyrics",
            "artist",
            "source",
            "views",
        ]

    region = RegionSerializer()
    artist = ArtistSerializer()
    source = MediaSourceSerializer()

from rest_framework import serializers

from artists.serializers import ArtistSerializer
from media.serializers import MediaSourceSerializer

from commons.transliteration import TransliterationSerializerMixin

from .models import Lullaby, Region


class NestedLullabySerializer(
    TransliterationSerializerMixin, serializers.ModelSerializer
):
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

    artist = ArtistSerializer()
    source = MediaSourceSerializer()


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["pk", "name", "slug", "lullabies"]

    lullabies = NestedLullabySerializer(many=True, read_only=True)


class NestedRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["pk", "name", "slug", "lullabies"]


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

    region = NestedRegionSerializer()
    artist = ArtistSerializer()
    source = MediaSourceSerializer()

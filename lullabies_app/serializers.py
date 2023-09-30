from rest_framework import serializers

from artists.serializers import NestedArtistSerializer

from .models import Lullaby


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = serializers.CharField(source="get_region_display")
    artists = NestedArtistSerializer(many=True)

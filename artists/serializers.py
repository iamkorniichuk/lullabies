from rest_framework import serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

    sex = serializers.CharField(source="get_sex_display")

from rest_framework import serializers

from commons.transliteration import TransliterationSerializerMixin

from .models import Artist


class ArtistSerializer(TransliterationSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "sex"]

    sex = serializers.CharField(source="get_sex_display")

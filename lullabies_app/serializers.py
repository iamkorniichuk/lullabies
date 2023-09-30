from rest_framework import serializers

from .models import Lullaby


class LullabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lullaby
        fields = "__all__"

    region = serializers.CharField(source="get_region_display")

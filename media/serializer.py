from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from .models import MediaSource


class MediaSource(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = MediaSource
        fields = "__all__"

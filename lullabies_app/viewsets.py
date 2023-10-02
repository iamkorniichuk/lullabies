from rest_framework import viewsets

from .serializers import LullabySerializer
from .models import Lullaby


class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LullabySerializer

    def get_queryset(self):
        allowed_formats = ("audio", "video")
        format = self.request.GET.get("format")
        if not format in allowed_formats:
            format = "objects"
        return getattr(Lullaby, format).all()

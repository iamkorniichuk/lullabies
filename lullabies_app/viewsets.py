from rest_framework import viewsets

from .serializers import LullabySerializer
from .models import Lullaby, MediaSource


class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LullabySerializer

    def get_queryset(self):
        format = self.request.GET.get("source-format")
        if format:
            sources = MediaSource.objects.filter(format=format).values_list(
                "pk", flat=True
            )
            return Lullaby.objects.filter(source__in=sources).all()
        return Lullaby.objects.all()

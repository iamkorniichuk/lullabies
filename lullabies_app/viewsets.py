from rest_framework import viewsets
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import LullabySerializer
from .models import Lullaby, MediaSource

source_format = openapi.Parameter(
    "source-format",
    openapi.IN_QUERY,
    description="Available formats: `audio`, `video`",
    required=False,
    type=openapi.TYPE_STRING,
)


@method_decorator(
    name="list", decorator=swagger_auto_schema(manual_parameters=[source_format])
)
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

from rest_framework import viewsets
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import filters

from media.models import MediaSource

from .serializers import ListLullabySerializer, DetailLullabySerializer
from .models import Lullaby


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
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Return lullaby with included source. Increment its `views` count.",
    ),
)
class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DetailLullabySerializer
        return ListLullabySerializer

    def get_object(self):
        instance = super().get_object()
        instance.views += 1
        instance.save()
        return instance

    def get_queryset(self):
        format = self.request.GET.get("source-format")
        if format:
            sources = MediaSource.objects.filter(format=format).values_list(
                "pk", flat=True
            )
            return Lullaby.objects.filter(source__in=sources).all()
        return Lullaby.objects.all()

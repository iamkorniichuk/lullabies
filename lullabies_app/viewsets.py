from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from commons.schema import languages_param
from media.models import MediaSource

from .serializers import LullabySerializer, RegionSerializer
from .models import Lullaby, Region
from .filtersets import LullabyFilterSet


source_format = openapi.Parameter(
    "source-format",
    openapi.IN_QUERY,
    description="Available formats: `audio`, `video`",
    required=False,
    type=openapi.TYPE_STRING,
)


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(manual_parameters=[source_format, languages_param]),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(manual_parameters=[languages_param]),
)
class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    queryset = Lullaby.objects.all()
    filterset_class = LullabyFilterSet
    serializer_class = LullabySerializer

    @action(detail=True, methods=["GET"])
    def increment_views(self, request, pk=None):
        instance = super().get_object()
        instance.views += 1
        instance.save()
        return Response({"views": instance.views})

    def get_queryset(self):
        queryset = super().get_queryset()
        source_format = self.request.query_params.get("source-format")
        if source_format:
            return self.filter_source_format(queryset, source_format)
        return queryset

    def filter_source_format(self, queryset, value):
        if not value:
            return queryset
        sources = MediaSource.objects.filter(format=value).values_list("pk", flat=True)
        return Lullaby.objects.filter(source__in=sources).all()


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "slug"

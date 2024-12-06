from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend

from commons.schema import languages_param

from .serializers import LullabySerializer, RegionSerializer
from .models import Lullaby, Region
from .filtersets import LullabyFilterSet, UseBoostOrderingFilter


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(manual_parameters=[languages_param]),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(manual_parameters=[languages_param]),
)
class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [UseBoostOrderingFilter, DjangoFilterBackend]
    queryset = Lullaby.objects.filter(is_visible=True).all()
    filterset_class = LullabyFilterSet
    serializer_class = LullabySerializer

    @action(detail=True, methods=["GET"])
    def increment_views(self, request, pk=None):
        instance = super().get_object()
        instance.views += 1
        instance.save()
        return Response({"views": instance.views})


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = "slug"

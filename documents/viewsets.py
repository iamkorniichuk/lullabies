from rest_framework import viewsets
from rest_framework.response import Response

from commons.utils import key_value_to_dict

from .serializers import DocumentSerializer
from .models import Document


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    pagination_class = None
    lookup_field = "name"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(key_value_to_dict(serializer.data, key="name", value="file"))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(key_value_to_dict([serializer.data], key="name", value="file"))

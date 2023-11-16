from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ContactSerializer
from .models import Contact


def contacts_to_dict(data):
    print(data)
    result = {}
    for obj in data:
        result[obj["name"]] = obj["value"]
    return result


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    pagination_class = None
    lookup_field = "name"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(contacts_to_dict(serializer.data))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(contacts_to_dict([serializer.data]))

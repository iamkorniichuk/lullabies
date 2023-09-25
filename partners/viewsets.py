from rest_framework import viewsets

from .serializers import PartnerSerializer
from .models import Partner


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

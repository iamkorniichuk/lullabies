from rest_framework import viewsets

from .serializers import LullabySerializer
from .models import Lullaby


class LullabyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LullabySerializer
    queryset = Lullaby.objects.all()

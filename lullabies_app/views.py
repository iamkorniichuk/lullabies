from django.db.models import Count
from rest_framework.views import APIView, Response

from .models import Lullaby


class LullabyStatisticView(APIView):
    def get(self, request, *args, **kwargs):
        data = Lullaby.objects.aggregate(
            lullabies=Count("pk"),
            regions=Count("region", distinct=True),
            artists=Count("artists", distinct=True),
        )
        return Response(data)

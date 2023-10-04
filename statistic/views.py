from django.db.models import Count
from rest_framework.views import APIView, Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from lullabies_app.models import Lullaby


class StatisticView(APIView):
    @swagger_auto_schema(
        responses={
            "200": openapi.Response(
                description="Amount statistic",
                examples={
                    "application/json": {
                        "lullabies": "100",
                        "regions": "13",
                        "artists": "25",
                    }
                },
            )
        }
    )
    def get(self, request, *args, **kwargs):
        data = Lullaby.objects.aggregate(
            lullabies=Count("pk"),
            regions=Count("region", distinct=True),
            artists=Count("artists", distinct=True),
        )
        return Response(data)

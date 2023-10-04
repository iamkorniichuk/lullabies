from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema

from .serializers import EmailSerializer


class SendEmailView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=EmailSerializer,
        responses={
            "200": "Email send",
            "400": "Bad request",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.send()
            return Response({"message": "Email send succesfully"}, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

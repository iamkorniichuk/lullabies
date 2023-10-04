from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import EmailSerializer


class SendEmailView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.send()
            return Response(
                {"message": "Email send succesfully"}, status=HTTP_202_ACCEPTED
            )

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

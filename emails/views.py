from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED
from rest_framework.parsers import MultiPartParser
from django.core.mail import EmailMessage

from contacts.models import Contact


class ConfiguredEmailMessage(EmailMessage):
    def __init__(self, subject, body, reply_to, *args, **kwargs):
        from_email = Contact.objects.get(name="Sender E-mail").value
        to = [Contact.objects.get(name="Recipient E-mail").value]
        super().__init__(
            subject=subject,
            body=body,
            from_email=from_email,
            to=to,
            reply_to=reply_to,
            *args,
            **kwargs,
        )


class SendEmailView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        subject = request.POST["theme"]
        body = request.POST["message"]
        email = [request.POST["email"]]
        body = f"Sender name: {name}\n" + body
        message = ConfiguredEmailMessage(subject, body, email)
        try:
            message.send(fail_silently=False)
        except Exception as error:
            report = error.message or error.report
            return Response(report, status=HTTP_400_BAD_REQUEST)
        return Response("Email send succesfully", status=HTTP_202_ACCEPTED)

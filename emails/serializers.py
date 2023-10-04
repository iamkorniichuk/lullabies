from django.core.validators import RegexValidator
from django.core.mail import EmailMessage
from rest_framework import serializers

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


class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(
        min_length=2,
        max_length=30,
        validators=[RegexValidator(r"^[A-Za-z'ʼ-\u04FF\u0400-\u04FF\s-]+$")],
    )
    email = serializers.EmailField(
        min_length=6,
        max_length=320,
        validators=[RegexValidator(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$")],
    )
    theme = serializers.CharField(min_length=6, max_length=320)
    message = serializers.CharField(max_length=600)

    def send(self):
        data = self.validated_data
        subject = data["theme"]
        body = f"Sender name: {data['name']}\n\n" + data["message"]
        reply_to = [data["email"]]

        email_message = ConfiguredEmailMessage(subject, body, reply_to)
        email_message.send()

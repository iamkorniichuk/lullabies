from django.core.validators import RegexValidator
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import serializers


class ConfiguredEmailMessage(EmailMessage):
    def __init__(self, subject, body, reply_to, *args, **kwargs):
        from_email = settings.EMAIL_SENDER
        to = [settings.EMAIL_RECIPIENT]
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
        min_length=1,
        max_length=30,
        validators=[RegexValidator(r"^[A-Za-z'ʼ-\u04FF\u0400-\u04FF\^s-]+$")],
    )
    email = serializers.EmailField(
        min_length=6,
        max_length=100,
        validators=[RegexValidator(r"^[a-z0-9._-]+@[a-z0-9.-]+.[a-z]{2,}$")],
    )
    theme = serializers.CharField(
        min_length=6,
        max_length=100,
        validators=[RegexValidator(r"^\S[^~`$@#{}\[\]\|/&]*\S$")],
    )
    message = serializers.CharField(
        min_length=1,
        max_length=600,
        validators=[RegexValidator(r"^\S[^~`$@#{}\[\]\|/&]*\S$")],
    )

    def send(self):
        data = self.validated_data
        subject = data["theme"]
        body = f"Sender name: {data['name']}\n\n" + data["message"]
        reply_to = [data["email"]]

        email_message = ConfiguredEmailMessage(subject, body, reply_to)
        email_message.send()

from django.urls import path

from .views import SendEmailView
from .apps import EmailsConfig

app_name = EmailsConfig.name

urlpatterns = [
    path("", SendEmailView.as_view(), name="main"),
]

from django.urls import path
from .views import LullabyStatisticView

urlpatterns = [
    path("statistic", LullabyStatisticView.as_view(), name="statistic"),
]

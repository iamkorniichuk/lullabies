from django.urls import path

from .views import StatisticView
from .apps import StatisticConfig

app_name = StatisticConfig.name

urlpatterns = [
    path("", StatisticView.as_view(), name="list"),
]

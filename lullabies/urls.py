from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from lullabies_app.viewsets import LullabyViewSet

router = DefaultRouter()
router.register("lullabies", LullabyViewSet, "lullaby")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from partners.viewsets import PartnerViewSet

router = DefaultRouter()
router.register("partners", PartnerViewSet, basename="partner")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

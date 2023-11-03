from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from partners.viewsets import PartnerViewSet
from contacts.viewsets import ContactViewSet
from lullabies_app.viewsets import LullabyViewSet

from .schema import schema_view


router = DefaultRouter()
router.register("lullabies", LullabyViewSet, basename="lullaby")
router.register("partners", PartnerViewSet, basename="partner")
router.register("contacts", ContactViewSet, basename="contact")

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/statistic/", include("statistic.urls")),
    path("api/email/", include("emails.urls")),
    path(
        "api/schema/",
        schema_view.with_ui(),
        name="schema",
    ),
]

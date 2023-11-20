from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from partners.viewsets import PartnerViewSet
from contacts.viewsets import ContactViewSet
from lullabies_app.viewsets import LullabyViewSet, RegionViewSet

from .schema import schema_view


router = DefaultRouter()
router.register("lullabies", LullabyViewSet, basename="lullaby")
router.register("regions", RegionViewSet, basename="region")
router.register("partners", PartnerViewSet, basename="partner")
router.register("contacts", ContactViewSet, basename="contact")

urlpatterns = [
    path("", include(router.urls)),
    path("statistic/", include("statistic.urls")),
    path("email/", include("emails.urls")),
    path(
        "schema/",
        schema_view.with_ui(),
        name="schema",
    ),
] + i18n_patterns(
    path("admin/", admin.site.urls),
    prefix_default_language=False,
)

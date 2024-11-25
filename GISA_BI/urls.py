from django.urls import path, include
from rest_framework.routers import DefaultRouter
from GISA_BI.views import GisaBIView

router = DefaultRouter()
router.register(r"gisa-bi", GisaBIView, basename="gisa-bi")

urlpatterns = [path("", include(router.urls))]

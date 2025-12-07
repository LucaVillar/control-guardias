# guardias/urls.py
from rest_framework.routers import DefaultRouter
from .views import NovedadViewSet  # + otros viewsets que tengas

router = DefaultRouter()
router.register(r"novedades", NovedadViewSet, basename="novedad")

urlpatterns = router.urls

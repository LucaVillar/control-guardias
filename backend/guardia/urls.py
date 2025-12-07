# tu_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuardiaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'guardias', GuardiaViewSet, basename='guardia')

urlpatterns = [
    path('', include(router.urls)),
]

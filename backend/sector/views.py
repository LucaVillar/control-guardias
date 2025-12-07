# guardias/views.py
from rest_framework import viewsets, permissions
from .models import Sector
from .serializers import SectorSerializer


class SectorViewSet(viewsets.ModelViewSet):
    """
    CRUD de Sectores.
    Por ahora solo accesible para usuarios admin.
    """
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAdminUser]

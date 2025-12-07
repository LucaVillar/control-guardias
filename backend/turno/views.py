# tu_app/views.py
from rest_framework import viewsets, permissions
from .models import Turno
from .serializers import TurnoSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [permissions.AllowAny]  # Ajustar más adelante

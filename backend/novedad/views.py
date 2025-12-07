# guardias/views.py
from rest_framework import viewsets, permissions
from .models import Novedad
from .serializers import NovedadSerializer


class NovedadViewSet(viewsets.ModelViewSet):
    """
    CRUD de novedades de guardia.
    """
    queryset = Novedad.objects.select_related("turno", "autor").all()
    serializer_class = NovedadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Seteamos el autor automáticamente con el usuario logueado
        serializer.save(autor=self.request.user)

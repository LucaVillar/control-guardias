# tu_app/views.py
from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # Para probar se puede poner AllowAny, pero en prod mejor controlar
    permission_classes = [permissions.AllowAny]

# tu_app/views.py
from rest_framework import viewsets, permissions
from .models import Guardia
from .serializers import GuardiaSerializer


class GuardiaViewSet(viewsets.ModelViewSet):
    queryset = Guardia.objects.all()
    serializer_class = GuardiaSerializer
    permission_classes = [permissions.AllowAny]  # después se ajusta

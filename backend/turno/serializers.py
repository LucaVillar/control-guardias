# tu_app/serializers.py
from rest_framework import serializers
from .models import Turno


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = [
            'id_turno',
            'guardia',
            'sector',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'estado',
            'observaciones',
        ]

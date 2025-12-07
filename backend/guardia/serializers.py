# tu_app/serializers.py
from rest_framework import serializers
from .models import Guardia


class GuardiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardia
        fields = [
            'id_guardia',
            'usuario',
            'legajo',
            'turno_habitual',
            'empresa',
            'fecha_alta',
            'fecha_baja',
        ]

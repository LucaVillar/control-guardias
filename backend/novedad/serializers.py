# guardias/serializers.py
from rest_framework import serializers
from .models import Novedad


class NovedadSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Novedad
        fields = [
            "id",            # id_novedad (PK)
            "turno",
            "autor",
            "autor_nombre",
            "titulo",
            "descripcion",
            "tipo",
            "fecha_hora",
            "prioridad",
            "adjunto",
            "creado_en",
            "actualizado_en",
        ]
        read_only_fields = ["id", "autor", "creado_en", "actualizado_en"]

    def get_autor_nombre(self, obj):
        if obj.autor:
            nombre = f"{obj.autor.first_name} {obj.autor.last_name}".strip()
            return nombre or obj.autor.username
        return None

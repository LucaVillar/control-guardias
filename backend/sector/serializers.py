# guardias/serializers.py
from rest_framework import serializers
from .models import Sector


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = [
            "id",          # id_sector (PK)
            "nombre",
            "descripcion",
            "empresa",
            "activo",
        ]
        read_only_fields = ["id"]

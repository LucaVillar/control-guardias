# tu_app/serializers.py
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'nombre',
            'apellido',
            'email',
            'password',
            'dni',
            'telefono',
            'rol',
            'activo',
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # no se devuelve en las respuestas
        }

    # OPCIONAL: si después quieren hashear la pass acá:
    # def create(self, validated_data):
    #     password_plana = validated_data.pop('password')
    #     usuario = Usuario(**validated_data)
    #     usuario.password = hashear_password(password_plana)
    #     usuario.save()
    #     return usuario

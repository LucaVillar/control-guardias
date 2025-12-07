# objetivo/models.py
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Empresa / Cliente"
        verbose_name_plural = "Empresas / Clientes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

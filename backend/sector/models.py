# guardias/models.py
from django.db import models


class Sector(models.Model):
    """
    Lugares donde se asignan guardias.
    """
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    empresa = models.CharField(max_length=150)  # Por ahora texto; después se puede pasar a FK Empresa
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"
        ordering = ["empresa", "nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"

# guardias/models.py
from django.db import models
from django.conf import settings
from turno.models import Turno
from guardia.models import Guardia
from sector.models import Sector
from usuarios.models import Usuario


class Novedad(models.Model):
    """
    El guardia registra eventos importantes durante su turno.
    """

    TIPO_CHOICES = [
        ("seguridad", "Seguridad"),
        ("mantenimiento", "Mantenimiento"),
        ("incidente", "Incidente"),
        ("aviso", "Aviso"),
        ("otros", "Otros"),
    ]

    PRIORIDAD_CHOICES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    # FK → Turno (modelo de la misma app guardias)
    turno = models.ForeignKey(
        "turno.Turno",  # si Turno está en esta misma app
        on_delete=models.CASCADE,
        related_name="novedades",
    )

    # FK → Usuario (modelo de auth)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="novedades_cargadas",
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="otros")
    fecha_hora = models.DateTimeField()  # se la mandás desde el frontend o usás ahora
    prioridad = models.CharField(
        max_length=10, choices=PRIORIDAD_CHOICES, default="media"
    )

    # adjunto opcional (imagen/archivo)
    adjunto = models.FileField(
        upload_to="novedades/",
        null=True,
        blank=True,
        help_text="Imagen o archivo relacionado a la novedad",
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"
        ordering = ["-fecha_hora", "-id"]

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"

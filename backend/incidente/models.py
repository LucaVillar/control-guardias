from django.db import models
from guardia.models import Guardia
from turno.models import Turno
from sector.models import Sector

class Incidente(models.Model):

    CLASIFICACION_CHOICES = [
        ("robo", "Robo"),
        ("accidente", "Accidente"),
        ("daño", "Daño"),
        ("intento", "Intento de delito"),
        ("otros", "Otros"),
    ]

    ESTADO_CHOICES = [
        ("abierto", "Abierto"),
        ("investigacion", "En investigación"),
        ("cerrado", "Cerrado"),
    ]

    id_incidente = models.AutoField(primary_key=True)
    turno = models.ForeignKey("turno.Turno", on_delete=models.CASCADE)
    sector = models.ForeignKey("sector.Sector", on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    clasificacion = models.CharField(max_length=20, choices=CLASIFICACION_CHOICES)
    nivel_gravedad = models.IntegerField()  # 1 al 5
    fecha_hora = models.DateTimeField(auto_now_add=True)
    reportado_por = models.ForeignKey("guardia.Guardia", on_delete=models.SET_NULL, null=True)
    adjunto = models.FileField(upload_to="incidentes_adjuntos/", null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="abierto")

    def __str__(self):
        return f"Incidente #{self.id_incidente} - {self.clasificacion}"

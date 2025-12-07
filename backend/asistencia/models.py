from django.db import models
from guardia.models import Guardia
from turno.models import Turno

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True, blank=True)

    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)

    ubicacion_entrada = models.CharField(max_length=255, null=True, blank=True)
    ubicacion_salida = models.CharField(max_length=255, null=True, blank=True)

    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia #{self.id_asistencia} - Guardia {self.guardia_id}"

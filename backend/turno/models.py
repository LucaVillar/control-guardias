# tu_app/models.py
from django.db import models   # Ajustá si Sector está en otra app
from guardia.models import Guardia
from sector.models import Sector


class Turno(models.Model):
    class EstadoTurno(models.TextChoices):
        PROGRAMADO = 'programado', 'Programado'
        EN_CURSO = 'en_curso', 'En curso'
        FINALIZADO = 'finalizado', 'Finalizado'
        AUSENTE = 'ausente', 'Ausente'

    id_turno = models.AutoField(primary_key=True)
    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE, related_name='turnos')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, choices=EstadoTurno.choices, default=EstadoTurno.PROGRAMADO)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Turno {self.id_turno} - {self.guardia.legajo} ({self.fecha})"

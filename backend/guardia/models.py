# tu_app/models.py
from django.db import models
from usuarios.models import Usuario  # si está en la misma app, esto alcanza


class Guardia(models.Model):
    class TurnoHabitual(models.TextChoices):
        MANANA = 'mañana', 'Mañana'
        TARDE = 'tarde', 'Tarde'
        NOCHE = 'noche', 'Noche'

    id_guardia = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='guardias')
    legajo = models.CharField(max_length=50, unique=True)
    turno_habitual = models.CharField(max_length=20, choices=TurnoHabitual.choices)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    fecha_alta = models.DateField()
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Guardia {self.legajo} - {self.usuario.nombre} {self.usuario.apellido}"

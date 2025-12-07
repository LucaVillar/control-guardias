from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("id_asistencia", "guardia", "fecha_entrada", "fecha_salida")
    list_filter = ("fecha_entrada", "fecha_salida")
    search_fields = ("guardia__usuario__nombre", "guardia__legajo")

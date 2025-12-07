from django.contrib import admin
from .models import Incidente

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = ("id_incidente", "clasificacion", "nivel_gravedad", "estado", "fecha_hora")
    list_filter = ("clasificacion", "estado", "nivel_gravedad")
    search_fields = ("descripcion",)

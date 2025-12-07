# guardias/admin.py
from django.contrib import admin
from .models import Novedad


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "tipo",
        "prioridad",
        "turno",
        "autor",
        "fecha_hora",
        "creado_en",
    )
    list_filter = ("tipo", "prioridad", "fecha_hora", "creado_en")
    search_fields = ("titulo", "descripcion", "autor__username", "autor__first_name", "autor__last_name")

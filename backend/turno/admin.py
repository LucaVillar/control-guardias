# tu_app/admin.py
from django.contrib import admin
from .models import Turno


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id_turno', 'guardia', 'sector', 'fecha', 'hora_inicio', 'hora_fin', 'estado')
    list_filter = ('estado', 'fecha', 'sector')
    search_fields = ('guardia__legajo', 'sector__nombre')

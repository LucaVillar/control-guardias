# tu_app/admin.py
from django.contrib import admin
from .models import Guardia


@admin.register(Guardia)
class GuardiaAdmin(admin.ModelAdmin):
    list_display = ('id_guardia', 'legajo', 'usuario', 'turno_habitual', 'empresa', 'fecha_alta', 'fecha_baja')
    list_filter = ('turno_habitual', 'empresa')
    search_fields = ('legajo', 'usuario__nombre', 'usuario__apellido')

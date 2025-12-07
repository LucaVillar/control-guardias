# objetivo/admin.py
from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "email", "telefono")

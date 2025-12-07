# guardias/admin.py
from django.contrib import admin
from .models import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "empresa", "activo")
    list_filter = ("empresa", "activo")
    search_fields = ("nombre", "empresa")

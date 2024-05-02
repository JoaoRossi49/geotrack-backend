from django.contrib import admin
from .models import Dispositivo, Coordenada

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'codigo', 'descricao')

@admin.register(Coordenada)
class CoordenadaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id', 'latitude', 'longitude', 'data_hora_inclusao', 'data_hora_coleta')

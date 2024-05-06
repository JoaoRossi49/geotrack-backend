from django.contrib import admin
from .models import Dispositivo, Coordenada, Veiculo

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'codigo', 'descricao')

@admin.register(Coordenada)
class CoordenadaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_id', 'latitude', 'longitude', 'data_hora_inclusao', 'data_hora_coleta')

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_veiculo', 'modelo_veiculo', 'placa', 'data_inclusao')
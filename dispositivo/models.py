from django.db import models

class Dispositivo(models.Model):
    codigo = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Coordenada(models.Model):
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    data_hora_coleta = models.DateTimeField()
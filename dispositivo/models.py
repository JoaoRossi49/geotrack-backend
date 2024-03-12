from django.db import models

class Dispositivo(models.Model):
    codigo = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
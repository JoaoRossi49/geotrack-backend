from django.db import models
from django.utils import timezone
from .signals import send_database_update_message


class Dispositivo(models.Model):
    codigo = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Coordenada(models.Model):
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    data_hora_coleta = models.DateTimeField()
    def save(self, *args, **kwargs):
        print("Chamou o save")
        send_database_update_message(True)
        if self.data_hora_coleta:
            self.data_hora_coleta = timezone.make_aware(self.data_hora_coleta)
        super().save(*args, **kwargs)      
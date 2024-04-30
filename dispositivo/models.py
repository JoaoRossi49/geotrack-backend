from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .signals import send_database_update_message
import uuid

class Dispositivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)

class Coordenada(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    data_hora_coleta = models.DateTimeField()
    def save(self, *args, **kwargs):
        send_database_update_message(True, self.latitude, self.longitude)
        if self.data_hora_coleta:
            self.data_hora_coleta = timezone.make_aware(self.data_hora_coleta)
        super().save(*args, **kwargs)      
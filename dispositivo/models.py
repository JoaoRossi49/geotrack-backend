from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .signals import send_database_update_message
import uuid

class Dispositivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Vínculo de dispositivo com usuário
    codigo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)

class Veiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Vínculo de veículo com usuário
    tipo_veiculo = models.CharField(max_length=20)
    modelo_veiculo = models.CharField(max_length=40)
    placa = models.CharField(max_length=7)
    data_inclusao = models.DateTimeField(auto_now_add=True)

class Coordenada(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dispositivo = models.ForeignKey(Dispositivo, default=uuid.uuid4, on_delete=models.CASCADE, blank=True, null=True) #Vínculo de coordenada com dispositivo
    veiculo = models.ForeignKey(Veiculo, default=uuid.uuid4, on_delete=models.CASCADE, blank=True, null=True) #Vínculo de coordenada com veículo
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    data_hora_inclusao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_hora_coleta = models.DateTimeField(blank=True, null=True)
    def save(self, *args, **kwargs):
        send_database_update_message(True, self.latitude, self.longitude)
        super().save(*args, **kwargs)      

    
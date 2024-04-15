from rest_framework import serializers
from .models import Dispositivo, Coordenada

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class CoordenadaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Coordenada
        fields = '__all__'
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dispositivo, Coordenada
from .serializers import DispositivoSerializer, CoordenadaSerializer
from rest_framework import generics
from rest_framework.views import APIView


class DispositivoList(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    
class DispositivoById(generics.RetrieveAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer    

class LastCoordenada(APIView):
    def get(self, request, format=None):
        last_coordenada = Coordenada.objects.last()
        if last_coordenada:
            return JsonResponse({
                'latitude': last_coordenada.latitude,
                'longitude': last_coordenada.longitude,
            })
        else:
            return JsonResponse({'error': 'Nenhuma coordenada encontrada'}, status=404)
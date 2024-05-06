from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dispositivo, Coordenada, Veiculo
from .serializers import DispositivoSerializer, UserSerializer, VeiculoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DispositivoList(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    
class DispositivoById(generics.RetrieveAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer 

class VeiculoList(generics.ListCreateAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    
class VeiculoById(generics.RetrieveAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer 

class LastCoordenada(APIView):
    def get(self, request, format=None):
        last_coordenadas = Coordenada.objects.order_by('-data_hora_coleta')[:5] 
        coordenadas_list = []
        for coordenada in last_coordenadas:
            coordenadas_list.append({
                'latitude': coordenada.latitude,
                'longitude': coordenada.longitude,
            })
        if coordenadas_list:
            return JsonResponse(coordenadas_list, safe=False)
        else:
            return JsonResponse({'error': 'Nenhuma coordenada encontrada'}, status=404)
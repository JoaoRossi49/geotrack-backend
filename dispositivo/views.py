from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dispositivo, Coordenada
from .serializers import DispositivoSerializer, CoordenadaSerializer, UserSerializer
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

class LastCoordenada(APIView):
    def get(self, request, format=None):
        last_coordenadas = Coordenada.objects.order_by('-id')[:5] 
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
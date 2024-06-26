from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dispositivo, Coordenada, Veiculo
from .serializers import DispositivoSerializer, UserSerializer, VeiculoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
        veiculos = ['b66b373b-b5b2-44ee-9cec-4bd3ec8dd584', 'fb97a02c-008b-4c34-ace1-31fdc5625000']
        last_n = 5

        coordenadas_list = []
        for veiculo_id in veiculos:
            last_coordenadas = Coordenada.objects.filter(veiculo_id=veiculo_id).order_by('-data_hora_coleta')[:last_n]
            for coordenada in last_coordenadas:
                coordenadas_list.append({
                    'veiculo': coordenada.veiculo.modelo_veiculo,
                    'latitude': coordenada.latitude,
                    'longitude': coordenada.longitude,
                })

        if coordenadas_list:
            return JsonResponse(coordenadas_list, safe=False)
        else:
            return JsonResponse({'error': 'Nenhuma coordenada encontrada'}, status=404)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            return Response({'authenticated': True})
        else:
            return Response({'authenticated': False})
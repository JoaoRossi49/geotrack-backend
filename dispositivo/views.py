from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dispositivo
from .serializers import DispositivoSerializer
from rest_framework import generics

class DispositivoList(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    
class DispositivoById(generics.RetrieveAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer    
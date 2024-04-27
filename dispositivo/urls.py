from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('dispositivos/', views.DispositivoList.as_view(), name='dispositivo-list'),
    path('dispositivos/<int:pk>/', views.DispositivoById.as_view(), name='dispositivo-detail'),
    path('coordenadas/last', views.LastCoordenada.as_view(), name='last_coordenada'),
    path('register/', views.CreateUserView.as_view(), name='register')
]

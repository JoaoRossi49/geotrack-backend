from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('dispositivos/', views.DispositivoList.as_view(), name='dispositivo-list'),
    path('dispositivos/<str:pk>/', views.DispositivoById.as_view(), name='dispositivo-detail'),
    path('veiculos/', views.VeiculoList.as_view(), name='Veiculo-list'),
    path('veiculos/<str:pk>/', views.VeiculoById.as_view(), name='Veiculo-detail'),
    path('coordenadas/last', views.LastCoordenada.as_view(), name='last_coordenada'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login')
]

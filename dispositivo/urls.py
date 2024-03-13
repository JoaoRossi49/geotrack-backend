from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('dispositivos/', views.DispositivoList.as_view(), name='dispositivo-list'),
    path('dispositivos/<int:pk>/', views.DispositivoById.as_view(), name='dispositivo-detail'),
]

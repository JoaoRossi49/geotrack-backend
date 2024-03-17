from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Mapa, name='mapa'),
]
urlpatterns += staticfiles_urlpatterns()
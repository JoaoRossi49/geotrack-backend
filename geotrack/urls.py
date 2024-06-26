from django.contrib import admin
from django.contrib.auth.urls import urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/', include('dispositivo.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/', urlpatterns),
    path('', include('mapa.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

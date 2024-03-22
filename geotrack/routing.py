from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from mapa.consumers import MapConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('map/', MapConsumer.as_asgi()),
    ]),
})
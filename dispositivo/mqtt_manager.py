import paho.mqtt.client as mqtt
import threading
from django.conf import settings
import json
from .models import Dispositivo, Coordenada

DispositivoManager = Dispositivo.objects

class MQTTManager:

    def __init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_message = self.on_message

        self.client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, settings.MQTT_KEEP_ALIVE_INTERVAL)
        self.client.subscribe(settings.MQTT_TOPIC, qos=1)

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode('utf-8'))
        codigo_dispositivo = payload.get('codigo_dispositivo')
        latitude = payload.get('latitude')
        longitude = payload.get('longitude')
        if DispositivoManager.filter(codigo=codigo_dispositivo).exists():
            coordenadas = Coordenada(
                latitude=latitude,
                longitude=longitude,
            )
            coordenadas.save()

    def start(self):
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.start()

mqtt_manager = MQTTManager()
mqtt_manager.start()
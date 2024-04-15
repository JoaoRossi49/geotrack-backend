import paho.mqtt.client as mqtt
import threading
from django.conf import settings
from datetime import datetime
import json
from .models import Dispositivo, Coordenada

DispositivoManager = Dispositivo.objects

class MQTTManager:

    def __init__(self):
        try:
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            self.client.on_message = self.on_message
            self.client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, settings.MQTT_KEEP_ALIVE_INTERVAL)
            self.client.subscribe(settings.MQTT_TOPIC, qos=0)
        except:
            print("Não foi possível conectar com o brooker")

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode('utf-8')
            payload = json.loads(payload)
            codigo_dispositivo = payload.get('codigo_dispositivo')
            latitude = payload.get('latitude')
            longitude = payload.get('longitude')
            if DispositivoManager.filter(codigo=codigo_dispositivo).exists():
                coordenadas = Coordenada(
                    latitude=latitude,
                    longitude=longitude,
                    data_hora_coleta=datetime.now(),
                )
                try:
                    coordenadas.save()
                except Exception:
                    raise Exception("Um erro ocorreu.")
        except Exception:
            Exception(f'Mensagem {msg.payload} não foi interpretada com sucesso!') 
    def start(self):
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.start()

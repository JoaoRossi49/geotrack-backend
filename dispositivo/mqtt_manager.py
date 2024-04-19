import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import threading
from datetime import datetime
import json
import pika

class MQTTManager:

    def __init__(self):
        try:
            load_dotenv()
            print(os.getenv('MQTT_BROKER'), os.getenv('MQTT_PORT'), os.getenv('MQTT_KEEP_ALIVE_INTERVAL'),  os.getenv('MQTT_TOPIC'))
            MQTT_BROKER = os.getenv('MQTT_BROKER')
            MQTT_PORT = os.getenv('MQTT_PORT')
            MQTT_KEEP_ALIVE_INTERVAL = os.getenv('MQTT_KEEP_ALIVE_INTERVAL')
            MQTT_TOPIC = os.getenv('MQTT_TOPIC')

            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            self.client.on_message = self.on_message
            self.client.connect(MQTT_BROKER, int(MQTT_PORT), int(MQTT_KEEP_ALIVE_INTERVAL))
            self.client.subscribe(MQTT_TOPIC, qos=0)
            print('Conectado ao brooker')
        except:
            print("Não foi possível conectar com o brooker")

    def on_message(self, client, userdata, msg):
        print('Recebeu mensagem')
        try:
            payload = json.loads(msg.payload.decode('utf-8'))
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()

            channel.queue_declare(queue='coordenadas')
            
            body = json.dumps(payload).encode('utf-8')
            routing_key = 'coordenadas'

            channel.basic_publish(exchange='', routing_key=routing_key, body=body)
            print(f'Enviado ao RabbitMQ usando a routing key: {routing_key}')
            connection.close()

        except Exception as e:
            print(f'Erro ao processar a mensagem: {e}')

    def start(self):
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.start()

import threading
from django.conf import settings
from datetime import datetime
import json, pika
import uuid
from .models import Dispositivo, Coordenada, Veiculo

DispositivoManager = Dispositivo.objects

class AMQPManager:

    def __init__(self):
        # Inicia a thread no construtor
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True  # Isso garante que a thread será fechada quando a aplicação principal terminar
        self.thread.start()

    def run(self):
        try:
            print('Tentando conexão com RabbitMQ')
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            print('Conectado ao RabbitMQ')

            channel.queue_declare(queue='coordenadas')

            def callback(ch, method, properties, body):
                try:
                    payload = body.decode('utf-8')
                    payload = json.loads(payload)
                    dispositivo_id = payload.get('dispositivo_id')
                    veiculo_id = payload.get('veiculo_id')
                    latitude = payload.get('latitude')
                    longitude = payload.get('longitude')                    
                    if DispositivoManager.filter(id=dispositivo_id).exists():
                        coordenadas = Coordenada(
                            id=uuid.uuid4(),
                            dispositivo = Dispositivo.objects.get(id=dispositivo_id),
                            veiculo = Veiculo.objects.get(id=veiculo_id),
                            latitude=latitude,
                            longitude=longitude,
                            data_hora_coleta=datetime.now(),
                        )
                        coordenadas.save()
                except Exception as e:
                    print(f"Erro ao processar mensagem: {str(e)}")

            channel.basic_consume(queue='coordenadas', on_message_callback=callback, auto_ack=True)
            print('Aguardando mensagens...')
            channel.start_consuming()
        except Exception as e:
            print(f"Não foi possível conectar com o broker: {str(e)}")


import threading
from django.conf import settings
from datetime import datetime
import json, pika
from django.core.cache import cache
from .models import Dispositivo, Coordenada

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
                    codigo_dispositivo = payload.get('codigo_dispositivo')
                    latitude = payload.get('latitude')
                    longitude = payload.get('longitude')

                    dispositivo = cache.get(f"dispositivo_{codigo_dispositivo}")

                    if not dispositivo:
                        dispositivo = DispositivoManager.filter(codigo=codigo_dispositivo).first()
                        cache.set(f"dispositivo_{codigo_dispositivo}", dispositivo, timeout=3600)

                    if dispositivo:
                        coordenadas = Coordenada(
                            latitude=latitude,
                            longitude=longitude,
                            data_hora_coleta=datetime.now(),
                        )
                        coordenadas.save()

                    cache.set(f"coordenadas_{dispositivo.id}", coordenadas, timeout=5)#3*24*60*60)

                    cache_keys = cache.get_many('*')

                    num_registros = len(cache_keys)

                    if cache_keys is not None:
                        # O registro está presente no cache, faça algo com os dados
                        print("Dados encontrados no cache:", num_registros)
                    else:
                        # O registro não está presente no cache, faça algo
                        print("Os dados não estão presentes no cache.")

                except Exception as e:
                    print(f"Erro ao processar mensagem: {str(e)}")

            channel.basic_consume(queue='coordenadas', on_message_callback=callback, auto_ack=True)
            print('Aguardando mensagens...')
            channel.start_consuming()
        except Exception as e:
            print(f"Não foi possível conectar com o broker: {str(e)}")


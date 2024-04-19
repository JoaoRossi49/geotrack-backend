from django.apps import AppConfig


class DispositivoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispositivo'

    def ready(self):
        from dispositivo.management.commands.amqp_manager import AMQPManager
        amqp_manager = AMQPManager()
        print('Iniciou o receiver AMQP')
        amqp_manager.handle()
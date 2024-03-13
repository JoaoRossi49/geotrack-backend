from django.apps import AppConfig


class DispositivoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispositivo'

    def ready(self):
        from dispositivo.management.commands.mqtt_manager import MQTTManager
        mqtt_manager = MQTTManager()
        mqtt_manager.handle()
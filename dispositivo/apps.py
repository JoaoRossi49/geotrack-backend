from django.apps import AppConfig


class DispositivoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispositivo'

    def ready(self):
        from django.core.management import call_command
        call_command('mqtt_manager')
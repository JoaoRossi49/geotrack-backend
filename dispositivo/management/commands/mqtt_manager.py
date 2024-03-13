from django.core.management.base import BaseCommand
from . import mqtt_manager

class Command(BaseCommand):
    help = 'Starts MQTTManager'

    def handle(self, *args, **options):
        mqtt_manager.mqtt_manager.start()
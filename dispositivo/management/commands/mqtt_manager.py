from django.core.management.base import BaseCommand
from ... import mqtt_manager

class MQTTManager(BaseCommand):
    help = 'Starts MQTTManager'

    def handle(self, *args, **options):
        mqtt_manager.MQTTManager().start()
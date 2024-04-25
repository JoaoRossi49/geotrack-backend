from django.core.management.base import BaseCommand
from ... import amqp_manager

class AMQPManager(BaseCommand):
    help = 'Starts AMQPManager'

    def handle(self, *args, **options):
        amqp_manager.AMQPManager()
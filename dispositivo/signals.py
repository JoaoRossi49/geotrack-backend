from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver

channel_layer = get_channel_layer()

def send_database_update_message(created):
    print("Enviou mensagem de atualização")
    print(created)
    if created:
        async_to_sync(channel_layer.group_send)(
            'map_room',
            {
                'type': 'send_message',
                'message': 'Database updated'
            }
        )
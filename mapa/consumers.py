import json
from channels.generic.websocket import WebsocketConsumer

class MapConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connected to the server'
        }))
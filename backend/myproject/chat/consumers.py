# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         self.accept()
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))
# 
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Get chat type and identifier from URL
        if "room_name" in self.scope["url_route"]["kwargs"]:
            self.chat_type = "room"
            self.identifier = self.scope["url_route"]["kwargs"]["room_name"]
            self.group_name = f"chat_room_{self.identifier}"
        elif "user_id" in self.scope["url_route"]["kwargs"]:
            self.chat_type = "individual"
            self.identifier = self.scope["url_route"]["kwargs"]["user_id"]
            self.group_name = f"chat_user_{self.identifier}"

        # Join group (room or individual)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave group (room or individual)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        recipient_id = text_data_json.get("recipient_id")  # For individual chats

        if self.chat_type == "room":
            # Send message to the room group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name, {"type": "chat.message", "message": message}
            )
        elif self.chat_type == "individual" and recipient_id:
            # Send message to the recipient's group
            recipient_group_name = f"chat_user_{recipient_id}"
            async_to_sync(self.channel_layer.group_send)(
                recipient_group_name, {"type": "chat.message", "message": message}
            )

    def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

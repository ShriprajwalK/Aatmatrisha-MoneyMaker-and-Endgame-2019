# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from .models import Company

"""

DJANGO CHANNELS PART. WEBSOCKETS PART. JS PART. NOT WORKING

"""

import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
#
# class TickTockConsumer(AsyncJsonWebsocketConsumer):
#
#     async def connect(self):
#         await self.accept()
#         while 1:
#             await asyncio.sleep(1)
#             await self.send_json("tick")
#             await asyncio.sleep(1)
#             await self.send_json(".....tock")
#

from channels.db import database_sync_to_async

class MyConsumer(WebsocketConsumer):
    async def connect(self):
        self.username = await database_sync_to_async(self.get_details)()

    def get_details(self):
        return Company.objects


from channels import Group

def ws_connect(message):
    print("Someone connected.")
    path = message['path']                                                      # i.e. /sensor/

    if path == b’/sensor/':
        print("Adding new user to sensor group")
        Group(“sensor").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({                                            # Reply to individual directly
           "text": "You're connected to sensor group :) ",
        })
    else:
        print("Strange connector!!")

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print("Received!!" + message['text'])

def ws_disconnect(message):
    print("Someone left us...")
    Group("sensor").discard(message.reply_channel)

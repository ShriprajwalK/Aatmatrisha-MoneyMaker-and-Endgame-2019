"""
DJANGO CHANNELS/JS/WEBSOCKETS PART. NOT WORKING.

"""


from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
#from .consumers import TickTockConsumer
from .consumers import MyConsumer
from . import views

application = [
        path("ws/", views.home,name='stockhome'),
    ]

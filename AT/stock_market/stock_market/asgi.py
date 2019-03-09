import os
import django
import channels.asgi
from channels.routing import get_default_application
#django.setup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock_market.settings")
channel_layer = channels.asgi.get_channel_layer()

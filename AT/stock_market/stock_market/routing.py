#My try at channels. Did not work.

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import stock_price.routing
from stock_price.consumers import ws_message, ws_connect, ws_disconnect

"""
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            stock_price.routing.application
        )
    ),
})
"""

channel_routing = {
    'websocket.connect': ws_connect,
    'websocket.receive': ws_message,
    'websocket.disconnect': ws_disconnect,
}

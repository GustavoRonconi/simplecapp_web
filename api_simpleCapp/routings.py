from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app_simpleCapp.consumers import NoseyConsumer
from .middleware import TokenAuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddlewareStack(
            URLRouter([path("notifications/", NoseyConsumer),])
        )
    }
)


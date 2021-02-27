from django.urls import path
from api.consumers import NotificationConsumer
from .middleware import TokenAuthMiddlewareStack

websocket_urlpatterns = [
    path("notification/", TokenAuthMiddlewareStack(NotificationConsumer.as_asgi())),
]


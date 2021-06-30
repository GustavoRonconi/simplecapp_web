from django.urls import path
from api.consumers import NotificationConsumer
from .middleware import TokenAuthMiddlewareStack

websocket_urlpatterns = [
    path("api/notification/", TokenAuthMiddlewareStack(NotificationConsumer.as_asgi())),
]

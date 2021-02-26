from django.urls import path
from app_simpleCapp.consumers import NotificationConsumer
from .middleware import TokenAuthMiddlewareStack

websocket_urlpatterns = [
    path("notification/", TokenAuthMiddlewareStack(NotificationConsumer.as_asgi())),
]


from django.urls import path
from app_simpleCapp.consumers import NotificationConsumer

websocket_urlpatterns = [
    path("notification/", NotificationConsumer.as_asgi()),
]


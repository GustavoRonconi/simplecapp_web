"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .middleware import TokenAuthMiddlewareStack
from .routings import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


application = ProtocolTypeRouter(
    {
        # Django's ASGI application to handle traditional HTTP requests
        "http": get_asgi_application(),
        # WebSocket chat handler
        "websocket": TokenAuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)


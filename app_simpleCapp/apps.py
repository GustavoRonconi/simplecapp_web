from django.apps import AppConfig


class AppSimpleCappConfig(AppConfig):
    name = "app_simpleCapp"

    def ready(self):
        from . import signals

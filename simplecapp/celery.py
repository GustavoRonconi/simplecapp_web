import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplecapp.settings")

celery_app = Celery("simplecapp")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")


for app_name in settings.INSTALLED_APPS:
    if app_name.startswith("django"):
        continue
    for root, dirs, files in os.walk(app_name + "/tasks"):
        for file in files:
            if (
                file.startswith("__")
                or file.endswith(".pyc")
                or not file.endswith(".py")
            ):
                continue
            file = file[:-3]
            celery_app.autodiscover_tasks([app_name + ".tasks"], related_name=file)


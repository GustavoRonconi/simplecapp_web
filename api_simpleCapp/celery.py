import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_simpleCapp.settings')

celery_app = Celery('api_simpleCapp')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
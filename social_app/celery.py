import os
import ssl
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings')

app = Celery('social_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
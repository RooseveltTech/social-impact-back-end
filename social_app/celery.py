import os
import ssl
from celery import Celery

# django_url = settings.CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings')

app = Celery('social_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
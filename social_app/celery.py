import os
import ssl
from celery import Celery
from django.conf import settings
url = settings.BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings')

app = Celery('social_app', broker=f'{url}')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
import os
import ssl
from celery import Celery
from django.conf import settings

url = settings._broker_url


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings')

app = Celery('social_app', broker_url=url, broker_use_ssl={'ssl_cert_reqs': ssl.CERT_NONE})

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','retoDjango.settings')

app = Celery('retoDjango')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()
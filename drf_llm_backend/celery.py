import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_llm_backend.settings")

app = Celery("drf_llm_backend")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# patch(celery=True)
celery_app = Celery("app", broker=settings.REDIS_PATH, backend=settings.REDIS_PATH)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@celery_app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

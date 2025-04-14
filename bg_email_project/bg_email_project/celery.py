from __future__ import absolute_import
import os
from celery import Celery

# set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bg_email_project.settings')

app = Celery('bg_email_project')

# config from settings.py using CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks from all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangolife.settings')

app = Celery('djangolife')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'celerycheck.task.send_mail_func',
        'schedule': crontab(hour=23, minute=15),
        #'args': (2,)
    }
    
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# we need to run two scheduler
#celery -A  djangolife beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
#celery -A  djangolife beat -l INFO


#celery -A  djangolife  worker -l INFO -P eventlet #its dynamic and easy to handle multiple reuqyest

#celery -A  djangolife  worker --pool=prefok --concurrency=5 --autoscale=10,3 -l info


#celery -A  djangolife  worker --pool=solo -l info


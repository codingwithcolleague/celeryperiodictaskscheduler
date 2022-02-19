from celery import shared_task
from django.utils import timezone
from datetime import timedelta

@shared_task
def add(x, y):
    return x + y


@shared_task(bind=True)
def send_mail_func(self):
    print("Now it running")
    return "Done"
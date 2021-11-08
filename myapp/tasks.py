from celery import shared_task

from time import sleep
from django.core.mail import send_mail
from django.conf import settings
@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task(email):

    sleep(50)
    send_mail(
        'Dear customer',
        'Thanks for your feedback',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return None

    


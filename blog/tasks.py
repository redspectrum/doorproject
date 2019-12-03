# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from time import sleep
from django.core.mail import send_mail


# @periodic_task(run_every=(crontab(minute='*/1')), name='my_first_task')
@periodic_task(run_every=timedelta(seconds=5), name='my_first_task')
def my_first_task():
    print('XXX'*20)


@shared_task
def my_second_tasks():
    print('YY'*20)


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task(email):
    EMAIL_HOST_USER = ''
    send_mail('Your biggest advantage', 'It is really work', EMAIL_HOST_USER, [email])
    print(email * 5)
    return True


@shared_task
def xsum(numbers):
    return sum(numbers)
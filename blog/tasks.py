# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from time import sleep
from django.core.mail import send_mail
from doorproject import settings
from datetime import datetime
from .models import Letter


# @periodic_task(run_every=(crontab(minute='*/1')), name='my_first_task')
# @periodic_task(run_every=timedelta(seconds=5), name='my_first_task')
# def my_first_task():
#     print('XXX'*20)

@shared_task
def send_email_task(email, title, body):
    send_mail(title, body, settings.EMAIL_HOST_USER, [email])


@shared_task
def send_email_letter():
    time_now = datetime.now()
    letters = Letter.objects.filter(sending_time__lt=time_now).order_by('-sending_time')
    message = []
    for letter in letters:
        try:
            send_email_task(email=letter.email_destination,
                            title=letter.title,
                            body=letter.body
                            )
        except Exception as e:
            message.append(
                "Error Mail {} to {} didn't send!".format(letter.email_destination, letter.email_destination))
            print('Error mail sending: {}'.format(e))
        else:
            message.append(
                'Mail {} to {} successfully sent!'.format(letter.email_destination, letter.email_destination))
        letter.delete()
    return message if message else ['No letters']
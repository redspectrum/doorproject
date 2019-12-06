#!/bin/bash

source .config/.config-env
export EMAIL_HOST EMAIL_PORT EMAIL_HOST_USER EMAIL_HOST_PASSWORD BACKEND_SECRET_KEY

python manage.py runserver &
celery -A doorproject worker -B -l INFO


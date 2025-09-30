#!/bin/sh
cd ./project

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata initial_data.json

# Создать или обнови суперпользователя
python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '1234')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
PY

gunicorn project.wsgi:application --bind 0.0.0.0:8000
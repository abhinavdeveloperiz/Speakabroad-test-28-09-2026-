#!/usr/bin/env bash
# Render build script for Speakabroad Django app
set -o errexit

pip install -r requirements.txt

python manage.py migrate --no-input
python manage.py loaddata app_data.json || true
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.filter(username='admin').first(); (u.set_password('admin'), u.save()) if u else User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
python manage.py collectstatic --no-input



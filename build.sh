#!/usr/bin/env bash
# Render build script for Speakabroad Django app
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

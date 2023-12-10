#!/bin/sh

cd RitmUS/
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
python populate_data.py
python manage.py runserver 0.0.0.0:8000 
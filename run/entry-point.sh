#! /bin/sh

python manage.py makemigrations
python manage.py migrate
uwsgi --ini run/uwsgi.ini

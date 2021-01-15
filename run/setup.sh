python manage.py makemigrations &&
python manage.py migrate &&
uwsgi --ini run/mysite.ini

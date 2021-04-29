#!bin/sh

set -e # Exit if there are an error

python manage.py collectstatic --noinput

# Command that runs our application using uWSGI 
uwsgi --socket :8000 --master --enable-threads --module app.wsgi


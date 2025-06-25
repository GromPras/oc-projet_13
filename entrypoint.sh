#!/usr/bin/env bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py loaddata fixtures/demo.json

exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT


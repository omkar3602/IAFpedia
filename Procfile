release: python manage.py migrate
web: gunicorn IAFpedia.wsgi --log-file -
heroku config:set DISABLE_COLLECTSTATIC=1
release: python3 manage.py migrate
web: daphne simplecapp.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery --app=simplecapp.celery worker -B --loglevel=info
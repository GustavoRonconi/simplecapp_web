release: python3 manage.py migrate
web: daphne api_simpleCapp.asgi:application --port 8000 --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2
web: daphne djangochat.asgi:application --port $PORT --bind 127.0.0.1 -v2
release: python manage.py migrate
worker: python manage.py runworker channels --settings=djangochat.settings -v2
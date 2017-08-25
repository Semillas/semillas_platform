web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn config.wsgi:application
daphne: daphne chat.asgi:channel_layer --port 8888 --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2

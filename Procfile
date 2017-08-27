web-alpha: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn config.wsgi:application
web: daphne --bind 0.0.0.0 --port $PORT chat.asgi:channel_layer -v2
worker: python manage.py runworker --settings config.settings.chat -v2

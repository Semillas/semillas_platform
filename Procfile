web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn config.wsgi:application
daphne: daphne chat.asgi:channel_layer -v2
worker: python manage.py --settings config.settings.chat runworker -v2

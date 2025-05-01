#!/bin/bash

# Only run DB migrations, Redis is handled separately
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

exec "$@"
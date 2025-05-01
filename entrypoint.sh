#!/bin/bash

# Start Redis in background
redis-server --daemonize yes

# Initialize database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Start Flask application
exec "$@"

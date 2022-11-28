#!/bin/bash
set -e

#echo "Wait until databases is ready"
#while ! nc -z "$DB_HOST" "${DB_PORT:-5432}"; do sleep 1; done;

# Apply migrations for both databases
#echo "Migrations for 'default' database..."
#python manage.py migrate --database=default

# echo "Starting Celery worker..."
#celery -A app worker -l INFO &
#celery -A app beat -l INFO &

exec "$@"
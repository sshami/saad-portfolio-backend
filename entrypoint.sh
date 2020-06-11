#!/bin/bash


# Verify that postgres is running and healthy before 
# applying migrations and running the Django development server
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while [ -z "$SQL_HOST" ] && [ -z "$SQL_PORT" ]
    do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input

echo "Running Django migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

exec "$@"

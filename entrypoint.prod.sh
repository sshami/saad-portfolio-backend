#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while [ -z "$SQL_HOST" ] && [ -z "$SQL_PORT" ]
    do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

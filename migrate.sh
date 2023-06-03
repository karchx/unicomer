#!/bin/bash
docker-compose -f docker-compose.dev.yml run --rm -it python-s python manage.py makemigrations
docker-compose -f docker-compose.dev.yml run --rm -it python-s python manage.py migrate

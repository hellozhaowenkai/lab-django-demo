#!/usr/bin/env bash

# Delete container & image
docker container rm -f lab-django-demo
docker image rm lab-django-demo:latest

# Build image
docker image build --tag=lab-django-demo:latest .

# Run container
docker container run \
  --user     $(id -u) \
  --name     lab-django-demo \
  --publish  10301:8888 \
  --volume   $PWD/logs:/app/logs \
  --volume   $PWD/databases:/app/databases \
  --volume   /dyai-app/lab-nginx/html/lab/django-demo/media:/app/media \
  --volume   /dyai-app/lab-secret/settings.private.toml:/app/config/settings.private.toml \
  --restart  unless-stopped \
  --interactive \
  --detach \
  lab-django-demo:latest

# Copy static files
docker cp lab-django-demo:/app/static/. /dyai-app/lab-nginx/html/lab/django-demo/static

# View logs
docker container logs lab-django-demo

#!/usr/bin/env bash

# Delete container & image
docker container rm -f lab-django-demo_dev
docker image rm lab-django-demo:dev

# Build image
docker image build --tag=lab-django-demo:dev .

# Run container
docker container run \
  --user     $(id -u) \
  --name     lab-django-demo_dev \
  --publish  10399:8888 \
  --volume   $PWD/logs:/app/logs \
  --volume   $PWD/databases:/app/databases \
  --volume   /dyai-app/lab-secret/settings.private.toml:/app/config/settings.private.toml \
  --restart  unless-stopped \
  --interactive \
  --detach \
  lab-django-demo:dev

# View logs
docker container logs lab-django-demo_dev

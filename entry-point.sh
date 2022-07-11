#!/bin/sh
# TODO: Need To Be Optimized.

# Default mode is DEVELOPMENT
# export DJANGO_SETTINGS_MODULE=my_site.config.development
MODE=development

# Get options
while getopts m:h OPT; do
  case ${OPT} in
    m)
      MODE=${OPTARG}
      ;;
    h)
      echo "Usage: $(basename $0) -m [development | production | testing]"
      exit
      ;;
  esac
done

# Run Django server
case ${MODE} in
  development)
    # DEVELOPMENT mode
    export DJANGO_SETTINGS_MODULE=my_site.config.${MODE}
    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ;;

  production)
    # PRODUCTION mode
    export DJANGO_SETTINGS_MODULE=my_site.config.${MODE}
    python manage.py collectstatic --no-input
    python manage.py makemigrations --no-input
    python manage.py migrate --no-input
    uwsgi --ini run/uwsgi.ini
    ;;

  testing)
    # TEST mode
    export DJANGO_SETTINGS_MODULE=my_site.config.${MODE}
    python manage.py test
    ;;
esac

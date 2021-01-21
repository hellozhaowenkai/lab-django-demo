#! /bin/sh
# TODO: Need To Be Optimized.

# Default mode is DEVELOPMENT
MODE=development

# Get options
while getopts "m:h" OPT; do
  case $OPT in
    m)
      MODE="$OPTARG"
      ;;
    h)
      echo "Usage: `basename $0` -m [development|production|test]"
      exit
      ;;
  esac
done

# Run Django server
case $MODE in
  development)
    # DEVELOPMENT mode
    export DJANGO_SETTINGS_MODULE=my_site.config.development
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ;;

  production)
    # PRODUCTION mode
    export DJANGO_SETTINGS_MODULE=my_site.config.production
    python manage.py makemigrations
    python manage.py migrate
    uwsgi --ini run/uwsgi.ini
    ;;

  test)
    # TEST mode
    export DJANGO_SETTINGS_MODULE=my_site.config.test
    python manage.py test
    ;;
esac

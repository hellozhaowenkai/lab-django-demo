"""
Django settings for my_site project in PRODUCTION mode.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


from my_site.config.base import *
from config import settings


DATABASES = {
    "sqlite3": DATABASES["sqlite3"],
    "mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "lab-django-demo",
        "USER": settings["secrets"]["mysql"]["user"],
        "PASSWORD": settings["secrets"]["mysql"]["password"],
        "HOST": "172.17.0.1",
        "PORT": "3306",
    },
}
DATABASES["default"] = DATABASES["sqlite3"]

FORCE_SCRIPT_NAME = settings["base"]["base-url"]

STATIC_URL = FORCE_SCRIPT_NAME + STATIC_URL
MEDIA_URL = FORCE_SCRIPT_NAME + MEDIA_URL

"""
Django settings for my_site project in BASE mode.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from my_site.settings import *


DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "my_app",
]

# LANGUAGE_CODE = "zh-hans"

USE_TZ = False
TIME_ZONE = "Asia/Shanghai"

# STATIC_URL = "./static/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# MEDIA_URL = "./media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = "my_app.MyUser"

from django.db import models
from django.contrib.auth.models import AbstractUser
from my_site.rest.models import APIModel


# Create your models here.


class MyUser(AbstractUser):
    pass


class LikeModel(APIModel):
    total_count = models.PositiveIntegerField(default=0)
    last_modified_by = models.GenericIPAddressField(default="172.0.0.1")
    last_modified_from = models.URLField(default="http://localhost/")

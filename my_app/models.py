from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from my_site.restful.models import APIModel


# Create your models here.


class MyUser(AbstractUser):
    pass


class Like(APIModel):
    total_count = models.PositiveIntegerField(default=0)
    last_modified_by = models.GenericIPAddressField(default="172.0.0.1")
    last_modified_from = models.URLField(default="http://localhost/")


class History(APIModel):
    modified_by = models.GenericIPAddressField(default="172.0.0.1")
    modified_from = models.URLField(default="http://localhost/")
    like = models.ForeignKey(Like, models.DO_NOTHING, blank=True, null=True)


@receiver(post_save, sender=Like)
def post_save_receiver(sender, instance, created, **kwargs):
    if not created:
        History.objects.create(
            like=instance,
            modified_by=instance.last_modified_by,
            modified_from=instance.last_modified_from,
        )

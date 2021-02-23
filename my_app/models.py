from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from my_site.restful.models import APIModel, APICounterField


# Create your models here.


class MyUser(AbstractUser):
    pass


class Like(APIModel):
    total_count = APICounterField(default=0)
    last_add_by = models.SmallIntegerField(default=0)
    last_modified_by = models.GenericIPAddressField(default="172.0.0.1")
    last_modified_from = models.URLField(default="http://localhost/")

    def update(self, **kwargs):
        last_add_by = kwargs.setdefault("last_add_by", 1)
        kwargs.setdefault("total_count", models.F("total_count") + last_add_by)

        return super().update(**kwargs)


class History(APIModel):
    add_by = models.SmallIntegerField("本次修改操作预期增加的点赞数", default=0)
    modified_by = models.GenericIPAddressField("本次修改操作来源 IP 地址", default="172.0.0.1")
    modified_from = models.URLField("本次修改操作来源 URL 地址", default="http://localhost/")
    # 所属点赞对象主键
    like = models.ForeignKey(Like, models.DO_NOTHING, blank=True, null=True)


@receiver(post_save, sender=Like)
def post_save_receiver(sender, instance, created, **kwargs):
    if not created:
        History.objects.create(
            like=instance,
            add_by=instance.last_add_by,
            modified_by=instance.last_modified_by,
            modified_from=instance.last_modified_from,
        )

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from my_site.restful.models import APIModel, APICounterField, disable_for_loaddata


# Create your models here.


class MyUser(AbstractUser):
    """
    自定义用户
    """

    pass


class Like(APIModel):
    """
    点赞信息
    """

    # 当前点赞总数
    total_count = APICounterField(default=0)
    # 最近修改操作预期增加的点赞数
    last_add_by = models.SmallIntegerField(default=0)
    # 最近修改操作来源 IP 地址
    last_modified_by = models.GenericIPAddressField(default="172.0.0.1")
    # 最近修改操作来源 URL 地址
    last_modified_from = models.URLField(default="http://localhost/")

    def update(self, **kwargs):
        last_add_by = kwargs.setdefault("last_add_by", 1)
        kwargs.setdefault("total_count", models.F("total_count") + last_add_by)

        return super().update(**kwargs)


class History(APIModel):
    """
    历史记录
    """

    # 本次修改操作预期增加的点赞数
    add_by = models.SmallIntegerField(default=0)
    # 本次修改操作来源 IP 地址
    modified_by = models.GenericIPAddressField(default="172.0.0.1")
    # 本次修改操作来源 URL 地址
    modified_from = models.URLField(default="http://localhost/")
    # 所属`点赞`对象主键
    like = models.ForeignKey(Like, models.DO_NOTHING, blank=True, null=True)


@disable_for_loaddata
@receiver(post_save, sender=Like)
def like_post_save_receiver(sender, instance, created, **kwargs):
    if created:
        return

    History.objects.create(
        like=instance,
        add_by=instance.last_add_by,
        modified_by=instance.last_modified_by,
        modified_from=instance.last_modified_from,
    )

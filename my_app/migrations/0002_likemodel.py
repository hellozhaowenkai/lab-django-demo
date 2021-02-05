# Generated by Django 3.1.5 on 2021-02-05 15:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikeModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("total_count", models.PositiveIntegerField(default=0)),
                ("last_modified_by", models.GenericIPAddressField(default="172.0.0.1")),
                ("last_modified_from", models.URLField(default="http://localhost/")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

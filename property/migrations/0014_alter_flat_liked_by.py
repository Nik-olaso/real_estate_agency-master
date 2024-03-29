# Generated by Django 5.0.1 on 2024-02-13 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0013_alter_owner_owners_flats"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="likes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Кто лайкнул",
            ),
        ),
    ]

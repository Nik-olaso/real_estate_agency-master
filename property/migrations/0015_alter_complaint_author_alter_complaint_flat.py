# Generated by Django 5.0.1 on 2024-02-13 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0014_alter_flat_liked_by"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaint",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="author_complain",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Кто жаловался",
            ),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="flat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="flat_complain",
                to="property.flat",
                verbose_name="Квартира, на которую жаловались",
            ),
        ),
    ]
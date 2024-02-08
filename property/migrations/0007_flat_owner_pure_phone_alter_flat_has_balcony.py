# Generated by Django 5.0.1 on 2024-02-01 15:43

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0006_flat_liked_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="owner_pure_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region="RU",
                verbose_name="Нормализованный номер владельца",
            ),
        ),
        migrations.AlterField(
            model_name="flat",
            name="has_balcony",
            field=models.BooleanField(
                blank=True, db_index=True, null=True, verbose_name="Наличие балкона"
            ),
        ),
    ]

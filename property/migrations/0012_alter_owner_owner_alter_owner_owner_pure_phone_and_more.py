# Generated by Django 5.0.1 on 2024-02-06 17:05

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0011_auto_20240206_1810"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="owner",
            field=models.CharField(
                db_index=True, max_length=200, verbose_name="ФИО владельца"
            ),
        ),
        migrations.AlterField(
            model_name="owner",
            name="owner_pure_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                db_index=True,
                max_length=128,
                null=True,
                region="RU",
                verbose_name="Нормализованный номер владельца",
            ),
        ),
        migrations.AlterField(
            model_name="owner",
            name="owners_phonenumber",
            field=models.CharField(
                db_index=True, max_length=20, null=True, verbose_name="Номер владельца"
            ),
        ),
    ]
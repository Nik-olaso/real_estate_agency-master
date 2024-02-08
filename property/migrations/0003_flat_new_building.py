# Generated by Django 2.2.24 on 2023-12-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0002_auto_20190829_2242"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="new_building",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Неизвестно"),
                    (True, "Новостройка"),
                    (False, "Старое здание"),
                ],
                default=None,
                max_length=30,
                null=True,
                verbose_name="Новостройка",
            ),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-13 15:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0015_alter_complaint_author_alter_complaint_flat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flat",
            name="owners_phonenumber",
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0012_alter_owner_owner_alter_owner_owner_pure_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="owners_flats",
            field=models.ManyToManyField(
                db_index=True,
                null=True,
                related_name="flats",
                to="property.flat",
                verbose_name="Квартиры в собственности",
            ),
        ),
    ]

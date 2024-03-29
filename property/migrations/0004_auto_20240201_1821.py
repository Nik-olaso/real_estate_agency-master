# Generated by Django 2.2.24 on 2024-02-01 15:21

from django.db import migrations


def new_building_or_not(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0003_flat_new_building"),
    ]

    operations = [
        migrations.RunPython(new_building_or_not),
    ]

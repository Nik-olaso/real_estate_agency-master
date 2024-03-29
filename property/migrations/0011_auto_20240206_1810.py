# Generated by Django 5.0.1 on 2024-02-06 15:10

from django.db import migrations


def fill_flat_to_owners(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    owners = Owner.objects.all()
    for owner in owners.iterator():
        owner.flats.set(Flat.objects.filter(owner=owner.name))
        owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0010_auto_20240201_1903"),
    ]

    operations = [migrations.RunPython(fill_flat_to_owners)]

from django.db import migrations
import phonenumbers


def create_valid_number(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(owner_pure_phone):
            owner_pure_phone = phonenumbers.format_number(
                owner_pure_phone, phonenumbers.PhoneNumberFormat.E164
            )
            flat.owner_pure_phone = owner_pure_phone
        else:
            flat.owner_pure_phone = None
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owner_pure_phone = ""
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0007_flat_owner_pure_phone_alter_flat_has_balcony"),
    ]

    operations = [
        migrations.RunPython(create_valid_number, move_backward),
    ]

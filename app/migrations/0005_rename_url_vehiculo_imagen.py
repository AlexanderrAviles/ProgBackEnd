# Generated by Django 4.1 on 2022-11-27 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_rename_imagen_vehiculo_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehiculo",
            old_name="url",
            new_name="imagen",
        ),
    ]

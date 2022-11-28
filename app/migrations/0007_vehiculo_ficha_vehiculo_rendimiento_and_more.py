# Generated by Django 4.1 on 2022-11-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_vehiculo_imagen_alter_vehiculo_precio"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiculo",
            name="ficha",
            field=models.FileField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vehiculo",
            name="rendimiento",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vehiculo",
            name="transmision",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
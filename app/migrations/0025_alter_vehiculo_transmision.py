# Generated by Django 4.1 on 2022-11-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0024_alter_vehiculo_transmision_delete_transmision"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiculo",
            name="transmision",
            field=models.CharField(max_length=30),
        ),
    ]

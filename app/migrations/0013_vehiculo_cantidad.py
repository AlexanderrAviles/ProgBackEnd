# Generated by Django 4.1 on 2022-11-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_alter_vehiculo_desctitulo_alter_vehiculo_desctitulo1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiculo",
            name="cantidad",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1 on 2022-11-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_vehiculo_desc_vehiculo_desc1_vehiculo_desc2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiculo",
            name="desc",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="vehiculo",
            name="desc1",
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name="vehiculo",
            name="desc2",
            field=models.CharField(max_length=2000),
        ),
    ]
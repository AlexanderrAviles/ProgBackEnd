# Generated by Django 4.1 on 2022-11-30 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_tipousuario_usuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transmision",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transmision", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="vehiculo",
            name="transmision",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.transmision"
            ),
        ),
    ]

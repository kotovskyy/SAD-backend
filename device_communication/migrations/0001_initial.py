# Generated by Django 5.0.4 on 2024-06-14 17:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("name", models.CharField(max_length=100)),
                ("mac_address", models.CharField(max_length=17)),
            ],
            options={
                "db_table": "device",
            },
        ),
        migrations.CreateModel(
            name="Device_type",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("device_type", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "device_type",
            },
        ),
        migrations.CreateModel(
            name="Measurement",
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
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("value", models.IntegerField()),
            ],
            options={
                "db_table": "measurement",
            },
        ),
        migrations.CreateModel(
            name="Measurement_type",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("unit", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "measurement_type",
            },
        ),
        migrations.CreateModel(
            name="Setting",
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
                ("value", models.IntegerField()),
            ],
            options={
                "db_table": "setting",
            },
        ),
        migrations.CreateModel(
            name="Setting_type",
            fields=[
                ("id", models.SmallAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("unit", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "setting_type",
            },
        ),
    ]

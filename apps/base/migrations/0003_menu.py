# Generated by Django 5.2.1 on 2025-05-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_newcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
    ]

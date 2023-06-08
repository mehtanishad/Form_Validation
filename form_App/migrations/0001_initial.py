# Generated by Django 4.2.2 on 2023-06-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
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
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(default="", max_length=50)),
                ("IsActive", models.BooleanField(default=False)),
            ],
            options={"db_table": "master",},
        ),
    ]

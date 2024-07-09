# Generated by Django 4.1.1 on 2022-10-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Login",
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
                (
                    "username",
                    models.CharField(
                        help_text="Enter the username here", max_length=30
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        help_text="Enter the password here", max_length=20
                    ),
                ),
            ],
        ),
    ]
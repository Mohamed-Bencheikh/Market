# Generated by Django 4.1.1 on 2022-10-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0009_alter_client_client_neckname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_photo",
            field=models.ImageField(upload_to="users"),
        ),
    ]

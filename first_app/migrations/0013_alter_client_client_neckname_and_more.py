# Generated by Django 4.1.1 on 2022-11-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0012_client_client_last_operation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_neckname",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="client",
            name="client_phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="client_photo",
            field=models.ImageField(default="user.png", upload_to="photos/"),
        ),
    ]

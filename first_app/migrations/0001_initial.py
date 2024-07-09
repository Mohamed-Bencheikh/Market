# Generated by Django 4.1.1 on 2022-09-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_age', models.IntegerField()),
                ('user_phone', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_passwd', models.CharField(max_length=100)),
            ],
        ),
    ]

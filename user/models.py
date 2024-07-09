from django.db import models


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, help_text="Enter the username here")
    password = models.CharField(max_length=20, help_text="Enter the password here")

    def __str__(self):
        return self.username

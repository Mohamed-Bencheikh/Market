from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_photo = models.ImageField(
        max_length=100, upload_to="photos/", default="user.png"
    )
    client_name = models.CharField(max_length=50, unique=True)
    client_neckname = models.CharField(max_length=50, default="", blank=True)
    client_phone = models.CharField(max_length=15, null=True, blank=True)
    client_total = models.BigIntegerField(default=0)
    client_last_payment = models.BigIntegerField(default=0)
    client_last_payment_date = models.DateTimeField(auto_now_add=True)
    client_last_operation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[" + self.client_name + ":" + str(self.client_id) + "]"

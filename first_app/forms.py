from django import forms
from django.contrib.auth import views

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("client_photo", "client_name", "client_neckname", "client_phone")

from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
from django.contrib.auth.decorators import login_required


def login(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        login_form.save()
        user = Login.objects.get(id=1)
        if (
            login_form.cleaned_data.get("username") == user.username
            and login_form.cleaned_data.get("password") == user.password
        ):
            return redirect("home")
    return render(request, "./login.html", {})


@login_required
def profile(request):
    return render(request, "./profile.html")

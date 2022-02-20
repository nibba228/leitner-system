from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    return render(request, 'accounts/login.html')


def registration(request):
    form = UserCreationForm()
    return render(request, 'accounts/registration.html', context={'form': form})

from django import forms
from django.contrib.auth.forms import UserCreationForm # user creation form
from django.contrib.auth.models import User # built in user model

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',]
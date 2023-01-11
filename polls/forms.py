from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    selection = (
        ('1', 'Male'),
        ('2', 'Female')
    )
    gender = forms.ChoiceField(required=True, choices=selection)

    class Meta:
        model = User
        fields = ("username", "email", "gender", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.gender = self.cleaned_data["gender"]

        if commit:
            user.save()
        return user

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# for the standard user rather than the creator
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
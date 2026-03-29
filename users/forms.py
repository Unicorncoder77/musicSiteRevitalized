from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password

# for the standard user rather than the creator

'''class UserPasswordField(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = userPasswords
        fields = ['password']
        widgets = {'password': forms.PasswordInput()}
    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.password = make_password(self.cleaned_data['password'])

        if commit:
            instance.save()

        return instance'''
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="username", max_length = 20, widget=forms.TextInput)
    email = forms.EmailField(label="email", widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput())
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    '''def save(self, commit=True):
        user = super().save(commit=False)
        if (commit):
            user.save()
        return user'''
    #password = forms.CharField(widget=forms.PasswordInput())
    #repeat_password = forms.CharField(widget=forms.PasswordInput())

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)


    
    
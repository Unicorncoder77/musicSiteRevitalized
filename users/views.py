from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from . import forms


# Create your views here.

def home(request):
    #template = loader.get_template('index.html')
    return render(request, 'index.html')

def userHome(request):
    return render(request, 'userHomePage.html')

def register(request):
    context = {}
    print("Request method: ", request.method)
    form = UserRegisterForm()
    #passForm = UserPasswordField()
    
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        # create form instance
        # check validity
        if (form.is_valid() ):
            print("valid form")
            #user = form.save(commit=False)
            #user.set_password(form.cleaned_data['password'])
            form.save()
            
            #login(request, form)
            return redirect('userHome')
       
        else:
            form = UserRegisterForm()
           
    return render(request, 'register.html', {'form': form})
    #else:
        #form = UserRegisterForm()
       # context['form'] = form
    #   return render(request, 'register.html', {'userForm': userForm, 'passForm': passForm})

def loginView(request):
    form = forms.UserLoginForm()
    if (request.method == 'POST'):
        form = forms.UserLoginForm(request.POST)
        if (form.is_valid()):
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'],)
            if (user is not None):
                login(request, user)
                return redirect('userHome')
                #message = f'Hello {user.username}! Welcome back!'
            else:
                return render(request, 'login.html', context={'form': form})
    return render(request, 'login.html', context={'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')
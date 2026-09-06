from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage 
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate, logout

@login_required
def reviewerHome(request):
    return render(request, 'templates/reviewerTemplate/userHomePage.html')


def register(request):
    context = {}
    print("Request method: ", request.method)
    form = UserRegisterForm()
    #passForm = UserPasswordField()
    
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        # create form instance
        # check validity
        if (form.is_valid()):
            print("valid form")
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(form.cleaned_data['password'])
            print(user.username)
            user.save()
            login(request, user)
            return redirect('userHome')
       
        else:
            form = UserRegisterForm()
           
    return render(request, 'register.html', {'form': form})
    

def loginView(request):
    form = forms.UserLoginForm()
    if (request.method == 'POST'):
        form = forms.UserLoginForm(request.POST)
        if (form.is_valid()):
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(form.cleaned_data)
            
            if (user is not None):
                print("Authenticated successfully")
                login(request, user)
                
                return redirect('userHome')
                #message = f'Hello {user.username}! Welcome back!'
            else:
                print("Authentication failed")
                print("User: ", user.username)
                print("INPUT: ", form.cleaned_data['username'], form.cleaned_data['password'])
                return render(request, 'login.html', context={'form': form})
            
    return render(request, 'login.html', context={'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required
def profile(request):
    context = {}
    #profile, created = Profile.objects.get_or_create(user=request.user)
    #userForm = UpdateUserForm(instance=request.user)
    #profileForm = UpdateProfileForm(instance=request.user)
    user = get_user_model()
    if (request.method == 'POST'):
        userForm = UpdateUserForm(request.POST, instance=request.user)
        #profileForm = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if (userForm.is_valid()):
            userForm.save()
            #profileForm.save()
            messages.success(request, "Your profile has been updated!")
            return redirect(to='profile')
    else:
        userForm = UpdateUserForm(instance=request.user)
        #profileForm = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'userForm': userForm})

@login_required 
def settings(request):
    return render(request, 'settings.html')

@login_required
def avatar(request):
    return render(request, 'avatar.html')

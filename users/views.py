from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Profile, Song, Review, Category 
from collections import defaultdict

# Create your views here.

def home(request):
    #template = loader.get_template('index.html')

    topReviews = Review.objects.select_related("song", "author").order_by("stars")

    groupedReviews = defaultdict(list)

    for topReview in topReviews:
        groupedReviews[topReview.song].append(topReview)

    
    songs = Song.objects.all()
    context = {"reviews" : dict(groupedReviews), "songs": songs}
    return render(request, 'index.html', context)

@login_required
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
        profileForm = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if (userForm.is_valid() and profileForm.is_valid()):
            userForm.save()
            profileForm.save()
            messages.success(request, "Your profile has been updated!")
            return redirect(to='profile')
    else:
        userForm = UpdateUserForm(instance=request.user)
        profileForm = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'userForm': userForm, 'profileForm': profileForm})

@login_required 
def settings(request):
    return render(request, 'settings.html')

@login_required
def avatar(request):
    return render(request, 'avatar.html');


def registerCreator(request):
    context = {}
    print("Request method: ", request.method)
    form = CreatorRegistrationForm()
    #passForm = UserPasswordField()
    
    if (request.method == 'POST'):
        form = CreatorRegistrationForm(request.POST)
        # create form instance
        # check validity
        if (form.is_valid()):
            print("valid form")
            #user = form.save(commit=False)
            #user.set_password(form.cleaned_data['password'])
            form.save()
            
            #login(request, form)
            return redirect('userHome')
       
        else:
            form = CreatorRegistrationForm()
           
    return render(request, 'creatorLogin.html', {'form': form})

def loginCreator(request):
    form = forms.CreatorLoginForm()
    if (request.method == 'POST'):
        form = forms.CreatorLoginForm(request.POST)
        if (form.is_valid()):
            creator = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(form.cleaned_data)
            
            if (creator is not None):
                print("Authenticated successfully")
                login(request, creator)
                
                return redirect('userHome')
                #message = f'Hello {user.username}! Welcome back!'
            else:
                print("Authentication failed")
                print("User: ", creator.username)
                print("INPUT: ", form.cleaned_data['username'], form.cleaned_data['password'])
                return render(request, 'creatorLogin.html', context={'form': form})
            
    return render(request, 'creatorLogin.html', context={'form': form})


@login_required
def createSong(request):
    if (request.method == 'POST'):
        form = SongForm(request.POST)
        if (form.is_valid()):
            song = form.save()
            return redirect("songDetail", song.id)
        
    else:
        form = SongForm()

    return render(request, "createSong.html", {"form": form})

def songDetail(request, id):
    song = get_object_or_404(Song, id=id)

    reviews = song.reviews.all()

    return render(request, "songDetail.html", {"song": song, "reviews": reviews})

@login_required
def createReview(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if (request.method == 'POST'):
        form = ReviewForm(request.POST)
        if (form.is_valid()):
            review = form.save(commit=False)

            review.author = request.user
            review.song = song
            review.save()

            return redirect("songDetail", id=song.id) 
    else:
        form = ReviewForm()

    context = {"song": song, "form":form}

    return render(request, "createReview.html", context)

def reviews(request):
    category = request.GET.get("category")
    reviews = Review.objects.select_related("song", "author").order_by("publication_date")
    songs = Song.objects.all()

    if (category):
        songs = songs.filter(category_type_id=category)

    categories = Category.objects.all()

    context = {"songs" : songs, "reviews": reviews, "categories": categories}

    return render(request, "reviews.html", context)

@login_required
def yourReviews(request):
   reviews = Review.objects.filter(author=request.user)

   context = {"reviews" : reviews}

   return render(request, "yourReviews.html", context)

def pleaseLogin(request):
    return render(request, "pleaseLogin.html")
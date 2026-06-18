from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Creator, Article, Review, Song, Category
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


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
    username = forms.CharField(label="Username", max_length = 20, widget=forms.TextInput)
    email = forms.EmailField(label="Email", widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
   
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
    password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'id': 'password'}))


class UpdateUserForm(forms.ModelForm):
    '''username = forms.CharField(label="Username", max_length=20, widget=forms.TextInput)
    email = forms.EmailField(label="Email", widget=forms.TextInput)'''
    print(User)

    class Meta: 
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label="avatar", widget=forms.FileInput)
    bio = forms.CharField(label="bio", widget=forms.Textarea)
    print(User)
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

# for the creator of articles
class CreatorRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label="fName", max_length=30, widget=forms.TextInput (attrs={'class' : 'fName ele'}))
    last_name = forms.CharField(label="lName", max_length=30, widget=forms.TextInput (attrs={'class': 'lName ele'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput (attrs={'class' : 'email ele'}))
    pen_name = forms.CharField(label="penName", max_length=30, widget=forms.TextInput (attrs={'class' : 'pName ele'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password' , 'class' : 'password ele'}))

    class Meta:
        model = Creator
        fields = ['first_name', 'last_name', 'email', 'pen_name', 'password']

class CreatorLoginForm(forms.Form):
    pen_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'pName ele'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'class' : 'password ele'}))

class SongForm(forms.ModelForm):
    title = forms.CharField(label="Song Title", max_length=30, widget=forms.TextInput)
    artist = forms.CharField(label="Song Artist",max_length=30,  widget=forms.TextInput)
    category_type = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a Category")
    collab = forms.BooleanField(label="Was this a collab?", required=False)
    single = forms.BooleanField(label="Was this released as a single?", required=False)
    release_year = forms.IntegerField(label="Enter the release year", validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today())])

    class Meta:
        model = Song
        fields = ['title', 'artist', 'category_type', 'collab', 'single']

class ReviewForm(forms.ModelForm):
    review_title = forms.CharField(label="Review Title", max_length=30, widget=forms.TextInput)
    review = forms.CharField(label="Review", widget=forms.Textarea)
    class Meta:
        model = Review
        fields = ['review_title', 'review', 'stars']
        widgets = {
            "stars": forms.RadioSelect(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    ]
            )
        }
      

    
    
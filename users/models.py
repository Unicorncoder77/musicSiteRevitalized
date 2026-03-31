from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    joined_date = models.DateField(auto_now_add=True, null=False)
    password = models.CharField(max_length=255, null=False)
    def save(self, *args, **kwargs):
        # hash if not hashed already
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # HANNA DOWNLOAD PILLOW ON OTHER LAPTOP TO USE THIS 
    avatar = models.ImageField(default='stockAvatar.jpg', upload_to='profile_images')
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if (img.height > 75 or img.width > 75):
            newImg = (75, 75)
            img.thumbnail(newImg)
            img.save(self.avatar.path)

    # standard str method that returns the username 
    def __str__(self):
        return self.user.username

'''class userPasswords(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)'''

    

"""
class Category(models.Model):
   category_name = models.CharField(max_length=255, null=True)
class Review(models.Model):
    review = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_title = models.CharField(max_length=255, null=True)
    # on_delete = cascade allows for everything from the user or the category to be deleted 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    publication_date = models.DateField(auto_now_add=True, null=True)

class Creator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    pen_name = models.CharField(max_length=255)
    joined_date = models.DateField(auto_now_add=True, null=True)
"""



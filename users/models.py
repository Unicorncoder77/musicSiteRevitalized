from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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

        if (img.height > 100 or img.width > 100):
            newImg = (100, 100)
            img.thumbnail(newImg)
            img.save(self.avatar.path)

    # standard str method that returns the username 
    def __str__(self):
        return self.user.username
    
# one to one would be better for a singular usage not linking a singular key to multiple items
# the foreign key would work for the rest of these use cases / many-to-one
class Category(models.Model):
   category_name = models.CharField(max_length=255, null=False)

   def __str__(self):
       return self.category_name

class Song(models.Model):
    title = models.CharField(max_length=40)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    artist = models.CharField(max_length=60)
    collab = models.BooleanField(null=False)


class Review(models.Model):
    review = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    review_title = models.CharField(max_length=255, null=False)
    # on_delete = cascade allows for everything from the user or the category to be deleted 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    publication_date = models.DateField(auto_now_add=True, null=False)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=False, related_name="reviews")

  # create a top reviews to make it easier to filter out (newest three or best rated perhaps)

class Creator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=False)
    pen_name = models.CharField(max_length=255)
    joined_date = models.DateField(auto_now_add=True, null=False)
    password = models.CharField(max_length=255, null=False)
    def save(self, *args, **kwargs):
        # hash if not hashed already
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Article(models.Model):
    article_title = models.CharField(max_length=255)
    article_contents = models.TextField()
    creator_id = models.ForeignKey(Creator, on_delete=models.CASCADE, null=False)
    publication_date = models.DateField(auto_now_add=True, null=False)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    article_cover = models.ImageField(default='stockAvatar.jpg', upload_to='cover_art')

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if (img.height > 100 or img.width > 100):
            newImg = (100, 100)
            img.thumbnail(newImg)
            img.save(self.avatar.path)





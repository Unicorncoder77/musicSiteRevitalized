from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    joined_date = models.DateField(auto_now_add=True, null=True)

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


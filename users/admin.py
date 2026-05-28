from django.contrib import admin
from .models import User, Profile, Category, Review, Creator, Article

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Creator)
admin.site.register(Article)
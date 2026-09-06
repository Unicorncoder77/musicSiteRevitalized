from django.contrib import admin
from .models import Reviewer, Category, Review, Creator, Article, Song

# Register your models here.
admin.site.register(Reviewer)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Creator)
admin.site.register(Article)
admin.site.register(Song)

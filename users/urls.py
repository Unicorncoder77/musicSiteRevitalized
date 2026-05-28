from django.urls import path 
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name="register"),
    path('home/', views.userHome, name='userHome'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('creatorLogin/', views.registerCreator, name='creatorLogin'),
    path('settings/', views.settings, name='settings'),
    path('avatar/', views.avatar, name='avatar'),
    #path('creatorLogin/', views.loginCreator, name='creatorLogin'),
   
]
from django.urls import path 
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name="register"),
    path('home/', views.userHome, name='userHome'),
    path('logout/', views.logoutUser, name='logout'),
   
]
from django.urls import path 
from .import views, reviewerView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', reviewerView.loginView, name='login'),
    path('register/', reviewerView.register, name="register"),
    path('home/', reviewerView.reviewerHome, name='userHome'),
    path('logout/', reviewerView.logoutUser, name='logout'),
    path('profile/', reviewerView.profile, name='profile'),
    #path('creatorLogin/', views.registerCreator, name='creatorLogin'),
    path('settings/', reviewerView.settings, name='settings'),
    path('avatar/', reviewerView.avatar, name='avatar'),
    path("songs/new/", views.createSong, name='createSong'),
    path("songs/<int:id>/", views.songDetail, name='songDetail'),
    path("songs/<int:song_id>/review/", views.createReview, name='createReview'),
    path('reviews/', views.reviews, name='reviews'),
    path('userReviews/', views.yourReviews, name='yourReviews'),
    path('pleaseLogin/', views.pleaseLogin, name='pleaseLogin'),
    #path('creatorPortal/', views.creatorPortal, name='creatorPortal'),
    #path('creatorHome/', views.creatorHome, name='creatorHome'),
    #path('creatorLogin/', views.loginCreator, name='loginCreator'),
    #path('creatorRegister/', views.registerCreator, name='registerCreator'),
    #path('creatorLogin/', views.loginCreator, name='creatorLogin'),
   
]
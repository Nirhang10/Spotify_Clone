from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home_page, name='Home_page'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('search/', views.search_view, name='search'),
    path('player/<int:track_id>/', views.musicPlayer_view, name='player'),
    path('playlist/<int:artist_id>/', views.playlist_view, name='playlist'),
    path('createplaylist/', views.createPlaylist_view, name='create_playlist'),
]

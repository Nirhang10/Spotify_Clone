from django.shortcuts import render
from .models import Song, Playlist, Artist
from django.db.models import Q
from .forms import RegisterForm, LoginForm, PlaylistForm
from django.shortcuts import get_object_or_404, redirect ,render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.


def Home_page(request):
    songs = Song.objects.all()
    play_song_id = request.GET.get('play', None)
    play_song = None

    if play_song_id:
        play_song = get_object_or_404(Song, id=play_song_id)


    return render(request, 'home.html', {'songs':songs, 'play_song':play_song})



def index(request):
    tracks = Song.objects.all()
    Artists = Artist.objects.all()
    return render(request, 'main/index.html', {'tracks':tracks, 'Artists':Artists})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        return render(request, 'main/login.html')   
       
    return render(request, 'main/login.html', {'form':form})

def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username=username, email=email, password=password)
            return redirect('index')
    else:
        form = RegisterForm()


    return render(request, 'main/signup.html', {'form':form})

def search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Song.objects.filter(Q(title__icontains= searched) | Q(artist__name__icontains=searched)) #Q help to filtering and Combine multiple conditions ( | = OR)
        search_results_count = venues.count()
        return render(request, 'main/search.html', {'searched':searched,'venues':venues,'search_results_count': search_results_count, 'user': request.user})
    else: 
        return render(request, 'main/search.html',{'tracks': [], 'search_results_count': 0, 'user': request.user})


def musicPlayer_view(request, track_id):
    play = get_object_or_404(Song, id=track_id)


    play_song_id = request.GET.get('play', None)
    play_song = None

    if play_song_id:
        play_song = get_object_or_404(Song, id=play_song_id)

    return render(request, 'main/music.html', {'play':play, 'play_song':play_song})


def createPlaylist_view(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()  # Save the many-to-many song relationship
            return render(request, 'main/createPlaylist.html', {'form': form, 'created': True})
    else:
        form = PlaylistForm()
    return render(request, 'main/createPlaylist.html', {'form': form})


def playlist_view(request, artist_id):
    path = get_object_or_404(Artist, id=artist_id)
    tracks = Song.objects.filter(artist=path) # Get all songs for this artist  
    return render(request, 'main/profile.html',{'path':path, 'tracks':tracks})
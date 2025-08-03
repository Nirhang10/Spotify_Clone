from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    artist_image = models.ImageField(upload_to='artist_image/', blank=True, null=True)
    name = models.CharField(max_length=50, default="Unknown Artist")

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=300, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists' )
    gerne = models.CharField(max_length=300, null=True)
    audio_url = models.CharField(max_length=300, null=False)
    duration = models.CharField(max_length=300, null=True)
    cover_image = models.ImageField(upload_to='cover_image/', blank=True, null=False)

    def __str__(self):
        return self.title
    

    def youtube_url_modify(self):
        if 'youtu.be' in self.audio_url:
            video_id = self.audio_url.split("/")[-1].split("?si=")[0]
        elif 'youtube.com' in self.audio_url:
            video_id = self.audio_url.split("v=")[-1].split("&")[0]

        return f"https://www.youtube.com/embed/{video_id}?autoplay=1&controls=0&showinfo=0&autohide=1"
    

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    song = models.ManyToManyField(Song, related_name='playlist')

    def __str__(self):
        return f"{self.name} - {self.user}"

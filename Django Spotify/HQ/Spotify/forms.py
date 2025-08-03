from django import forms
from .models import Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    lables = {
            'username':'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Repeat Password'
    }

    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
class SearchForm(forms.Form):
    search_query = forms

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name', 'song')


class userRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        lables = {
            'username':'Username',
            'email':'Email',
            'password1':'Passwordqq',
            'password2':'Repeat Password'
        }
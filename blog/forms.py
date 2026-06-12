from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'immagine',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', 'immagine',)

class RegistrazioneForm(UserCreationForm):
    email = forms.EmailField(required=True) # Rende il campo email obbligatorio

    class Meta:
        model = User
        fields = ('username', 'email') # I campi che l'utente vedrà nella pagina
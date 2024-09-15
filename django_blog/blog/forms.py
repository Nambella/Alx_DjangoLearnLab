from django import forms
from .models import posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['title', 'content']
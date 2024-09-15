from django import forms
from taggit.forms import TagWidget
from .models import posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Post, Tag
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
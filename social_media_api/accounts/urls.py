from django.urls import path
from .views import RegisterView, LoginView
from .views import follow_user, unfollow_user
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]

# posts/urls.py
from django.urls import path
from .views import feed

urlpatterns = [
    path('feed/', feed, name='feed'),
]


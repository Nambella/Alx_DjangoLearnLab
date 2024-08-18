# relationship_app/urls.py
app_name = 'relationship_app'

# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='book-list'),

    # Class-based view (with library ID as a parameter)
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library-detail'),
]

from django.contrib.auth import views as auth_views

urlpatterns = [
    # ...
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # Add other authentication views here...
]

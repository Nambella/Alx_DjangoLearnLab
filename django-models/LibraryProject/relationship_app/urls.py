# relationship_app/urls.py
app_name = 'relationship_app'

# relationship_app/urls.py
from django.urls import path
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add_book/', add_book, name='add-book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit-book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete-book'),
]  
    
urlpatterns = [
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),
]
from .views import list_books, LibraryDetailView
"views.register", "LogoutView.as_view(template_name="
urlpatterns = [
    # Function-based view
    path('books/', list_books, name='book-list'),

    # Class-based view (with library ID as a parameter)
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library-detail'),
]

from django.contrib.auth import views as auth_views
path('register/', auth_views.RegisterView.as_view(template_name='registration/register.html'), name='register'),

urlpatterns = [
    # ...
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), template_name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # Add other authentication views here...

]

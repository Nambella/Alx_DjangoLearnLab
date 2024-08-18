# relationship_app/urls.py
app_name = 'relationship_app'

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='book-list'),

    # Class-based view (with library ID as a parameter)
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library-detail'),
]

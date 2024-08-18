# relationship_app/views.py
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Library, Book
from .models import Book


class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.all.filter(library__id=library_id)
"relationship_app/list_books.html", "Book.objects.all()"

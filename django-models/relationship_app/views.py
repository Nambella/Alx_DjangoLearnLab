# relationship_app/views.py
from django.views.generic import ListView
from .models import Library, Book

class LibraryDetailView(ListView):
    model = Book
    template_name = 'library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.all.filter(library__id=library_id)
"relationship_app/list_books.html", "Book.objects.all()"
["relationship_app/library_detail.html"]
from django.shortcuts import render

# relationship_app/views.py
from django.shortcuts import render
from .models import Book  

def list_books(request):
    books = books.objects.all()
    return render(request, 'books_list.html', {'books': books})

from django.views.generic import ListView
from .models import Library, Book

class LibraryDetailView(ListView):
    model = Book
    template_name = 'library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.filter(library__id=library_id)

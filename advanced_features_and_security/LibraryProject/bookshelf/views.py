from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    # Your edit view logic here
    pass
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Specify your own template name/location
    context_object_name = 'book_list'  # Use 'book_list' as the template variable name

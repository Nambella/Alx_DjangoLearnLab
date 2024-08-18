from django.shortcuts import render

# Create your views here.
# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Import your model(s)

def list_books(request):
    books = books.objects.all()
    return render(request, 'books_list.html', {'books': books})

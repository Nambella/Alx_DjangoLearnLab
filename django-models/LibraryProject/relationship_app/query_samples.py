# relationship_app/query_samples.py

from relationship_app.models import Author, Book

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(authors=author)
        return books
    except Author.DoesNotExist:
        return []

from relationship_app.models import Book

def get_all_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    return books

from relationship_app.models import Library

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None




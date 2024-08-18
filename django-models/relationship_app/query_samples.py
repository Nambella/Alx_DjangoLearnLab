# relationship_app/query_samples.py

from relationship_app.models import Author, Book

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return []

# Example usage:
author_name = "J.K. Rowling"
books_by_author = get_books_by_author(author_name)
for book in books_by_author:
    print(f"Book by {author_name}: {book.title}")

from relationship_app.models import Book

def get_all_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    return books

# Example usage:
library_name = "Central Library"
all_books_in_library = get_all_books_in_library(library_name)
for book in all_books_in_library:
    print(f"Book in {library_name}: {book.title}")
    
from relationship_app.models import Library

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None

# Example usage:
library_name = "Main Street Library"
librarian = get_librarian_for_library(library_name)
if librarian:
    print(f"Librarian for {library_name}: {librarian.name}")
else:
    print(f"No librarian found for {library_name}")

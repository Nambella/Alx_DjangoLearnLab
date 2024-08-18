# query_samples.py

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        all_books = Book.objects.filter(library=library)
        print(f"Books in {library_name}:")
        for book in all_books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Librarian for {library_name}: {library.librarian}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

# Example usage:
if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    list_all_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")




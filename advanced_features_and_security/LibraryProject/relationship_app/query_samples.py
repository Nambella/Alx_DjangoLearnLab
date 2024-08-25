# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    return books_by_author

# List all books in a library
def get_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    all_books_in_library = library.books.all()
    return all_books_in_library

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    librarian =Librarian.objects.get(library=library_name)
    return librarian

# Example usage:
if __name__ == "__main__":
    # Replace with actual names
    author_name = "J.K. Rowling"
    library_name = "Hogwarts Library"

    books_by_author = get_books_by_author(author_name)
    all_books_in_library = get_all_books_in_library(library_name)
    librarian = get_librarian_for_library(library_name)

    print(f"Books by {author_name}: {books_by_author}")
    print(f"All books in {library_name}: {all_books_in_library}")
    print(f"Librarian for {library_name}: {librarian}")




from relationship_app.models import Book

def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

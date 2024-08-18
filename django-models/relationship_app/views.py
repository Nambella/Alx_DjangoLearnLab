# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Library, Book
from .models import Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    # Your librarian view logic here
    return render(request, 'librarian_view.html')
@user_passes_test(is_member)
def member_view(request):
    # Your member view logic here
    return render(request, 'member_view.html')
class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.all.filter(library__id=library_id)
"relationship_app/list_books.html", "Book.objects.all()"

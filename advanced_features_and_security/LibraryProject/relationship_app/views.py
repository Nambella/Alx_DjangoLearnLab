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
from django.contrib.auth.decorators import permission_required

@permission_required("relationship_app.can_add_book")
def add_book(request):
    # Your book creation logic here
    return render(request, 'add_book.html')

@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    # Your book editing logic here
    return render(request, 'edit_book.html')

@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    # Your book deletion logic here
    return render(request, 'delete_book.html')

def has_admin_permissions(user):
    return user.userprofile.role == 'Admin' and user.userprofile.can_view_admin_panel

@user_passes_test(has_admin_permissions)
def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_view.html')
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
def create_admin_user(username, password):
    user = user.objects.create_user(username=username, password=password)
    user_profile = UserProfile.objects.create(user=user, role='Admin')
    user_profile.can_view_admin_panel = True
    user_profile.can_manage_users = True
    user_profile.save()


class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.all.filter(library__id=library_id)
"relationship_app/list_books.html", "Book.objects.all()"

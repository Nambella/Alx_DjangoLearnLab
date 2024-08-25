from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    # Your edit view logic here
    pass
from django.views.generic import ListView
from .models import Book
from .forms import ExampleForm
from django.shortcuts import render

def my_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            # Redirect to a success page or render a template
            pass
    else:
        form = ExampleForm()

    return render(request, 'form_example.html', {'form': form})

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Specify your own template name/location
    context_object_name = 'book_list'  # Use 'book_list' as the template variable name
def book_list(request):
    books = Book.objects.all()
    # Your view logic here
    return render(request, 'books/book_list.html', {'books': books})
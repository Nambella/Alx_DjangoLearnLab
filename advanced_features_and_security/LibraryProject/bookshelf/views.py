from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    # Your edit view logic here
    pass

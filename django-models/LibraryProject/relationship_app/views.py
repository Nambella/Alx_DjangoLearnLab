from django.shortcuts import render

# Create your views here.
# relationship_app/views.py
from django.shortcuts import render
from .models import models # Import your model(s)

def my_view(request):
    # Your view logic here
    queryset = YourModel.objects.all()
    return render(request, 'your_template.html', {'queryset': queryset})

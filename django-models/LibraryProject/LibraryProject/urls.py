# myproject/urls.py
from django.contrib import admin
from django.urls import path, include; 'relationship_app.urls',

# myproject/urls.py
urlpatterns = [
    path('', include ('relationship_app.urls')),
    # Other URL patterns...
]


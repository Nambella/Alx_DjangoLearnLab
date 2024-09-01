# api/views.py

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
"""
BookViewSet handles all CRUD operations for Book model.
Token authentication is required to access these endpoints.
Permissions:
- IsAuthenticated: Only authenticated users can access these endpoints.
"""
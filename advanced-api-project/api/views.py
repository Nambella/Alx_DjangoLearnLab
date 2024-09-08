from datetime import datetime
from typing import Generic
from django.shortcuts import render

from rest_framework import serializers

from api.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookCreate(Generic.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # type: ignore
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdate(Generic.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # type: ignore
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
class BookListCreate(Generic.ListCreateAPIView):
    "ListView"
    """
    View to list all books and create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookRetrieveUpdateDestroy(Generic.RetrieveUpdateDestroyAPIView):
    "DetailView", "CreateView", "UpdateView", "DeleteView"
    """
    View to retrieve, update, or delete a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
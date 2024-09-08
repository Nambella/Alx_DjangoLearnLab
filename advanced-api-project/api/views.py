from datetime import datetime
from typing import Generic
from django.shortcuts import render

from rest_framework import serializers

from api.models import Book
from rest_framework.permissions import IsAuthenticated

class BookCreate(Generic.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # type: ignore
    permission_classes = [IsAuthenticated]

class BookUpdate(Generic.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # type: ignore
    permission_classes = [IsAuthenticated]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

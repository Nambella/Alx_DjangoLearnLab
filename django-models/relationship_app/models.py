# relationship_app/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    # Other fields (e.g., publication date, genre, etc.)

class Library(models.Model):
    name = models.CharField(max_length=200)
    librarian = models.ForeignKey('Librarian', on_delete=models.SET_NULL, null=True)
    # Other fields (e.g., location, opening hours, etc.)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # Other fields (e.g., contact information, etc.)

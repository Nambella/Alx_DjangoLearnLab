# relationship_app/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    librarian = models.ForeignKey('Librarian', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


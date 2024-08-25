# bookshelf/models.py

from django.db import models
# Import necessary modules
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Add any other custom fields relevant to your application

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    

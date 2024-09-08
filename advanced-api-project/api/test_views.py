from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    def test_retrieve_book(self):
        url = reverse('book-retrieve-update-destroy', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter')

    def test_update_book(self):
        url = reverse('book-retrieve-update-destroy', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-retrieve-update-destroy', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        url = reverse('book-list-create') + '?title=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_search_books(self):
        url = reverse('book-list-create') + '?search=Harry'
        response = self.client.get(url)
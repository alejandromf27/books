from django.contrib.auth.models import User
from django.db import connection
from rest_framework.test import APITestCase
from rest_framework import status

from library.models import Book, Author


class BookTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        leo_tolstoy = Author.objects.create(name='Leo Tolstoy')
        alexandre_dumas = Author.objects.create(name='Alexandre Dumas')

        Book.objects.create(title='War and Peace', author=leo_tolstoy)
        Book.objects.create(title='Anna Karenina', author=leo_tolstoy)
        Book.objects.create(title='Resurrection', author=leo_tolstoy)
        Book.objects.create(title='The Three Musketeer', author=alexandre_dumas)
        Book.objects.create(title='The Count of Monte Cristo', author=alexandre_dumas)

    def test_book_list(self):
        with self.assertNumQueries(1):
            response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_author_list(self):
        with self.assertNumQueries(2):
            response = self.client.get('/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_author_count_books_list(self):
        with self.assertNumQueries(2):
            response = self.client.get('/authors_books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

from rest_framework import viewsets

from library.models import Book, Author
from library.serializers import BookSerializer, AuthorSerializer, AuthorCountSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        books = Book.objects.select_related('author').order_by('title')
        return books


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        authors = Author.objects.prefetch_related('books').order_by('name')
        return authors


class AuthorCountViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorCountSerializer

    def get_queryset(self):
        authors = Author.objects.prefetch_related('books').order_by('name')
        return authors

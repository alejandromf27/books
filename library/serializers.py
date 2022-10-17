from rest_framework import serializers

from library.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author']

    @staticmethod
    def get_author(obj):
        return obj.author.name


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'books']

    @staticmethod
    def get_books(obj):
        return ", ".join([b.title for b in obj.books.all()])


class AuthorCountSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'total']

    def get_total(self, obj):
        return obj.books.count()

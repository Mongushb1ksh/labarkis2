from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Отобразит всю информацию об авторе

    class Meta:
        model = Book
        fields = '__all__'
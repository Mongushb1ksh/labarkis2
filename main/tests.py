from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Author, Book
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Автор 1", biography="Биография автора 1")
        self.book = Book.objects.create(
            title="Книга 1",
            author=self.author,
            publication_year=2020,
            genre="Жанр 1",
            category="fiction",
            publisher="Издательство 1",
            cover_image="image.jpg",
            book_file="book.pdf"
        )

    def test_get_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_books(self):
        url = reverse('book-list') + '?q=Книга 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
# Create your tests here.

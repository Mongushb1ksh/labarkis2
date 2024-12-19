from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsAdminUserOrReadOnly


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Только администраторы могут добавлять книги.")
        serializer.save()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SearchBooks(APIView):
    def get(self, request):
        query_params = request.query_params
        books = Book.objects.all()

        if 'title' in query_params:
            books = books.filter(title__icontains=query_params['title'])
        if 'genre' in query_params:
            books = books.filter(genre__icontains=query_params['genre'])
        if 'author' in query_params:
            authors = Author.objects.filter(first_name__icontains=query_params['author'],  last_name__icontains = query_params['author'])
            books = books.filter(author__in=authors)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
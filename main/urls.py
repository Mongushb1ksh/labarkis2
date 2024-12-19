from django.urls import include, path
from .views import BookList, BookDetail, AuthorList, AuthorDetail, SearchBooks

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('search/', SearchBooks.as_view(), name='search-books'),
]
from django.urls import path
from .views import BookListCreateView, BookDetailView
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BookListView
from .views import (
    BookListView,
    BookUpdateView,
    BookDeleteView,
    BookCreateView,  
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books-viewset', BookViewSet)


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

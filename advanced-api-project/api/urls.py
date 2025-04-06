from django.urls import path
from .views import BookListCreateView, BookDetailView
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BookListView

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books-viewset', BookViewSet)


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]

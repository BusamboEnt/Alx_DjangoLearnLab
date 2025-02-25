from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view
from .views import BookDetailView
from .views import BookListView

urlpatterns = [
    path("books/", list_books, name="list_books"),  
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookListView.as_view(), name='list_books'),  
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]

from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view
from .views import BookDetailView
from .views import BookListView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookListView.as_view(), name='list_books'),  
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
]

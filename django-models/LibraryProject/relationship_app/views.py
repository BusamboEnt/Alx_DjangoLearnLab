from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book
from .models import Library

def homepage(request):
    return render(request, 'relationship_app/homepage.html')

def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"    
class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"   
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"       
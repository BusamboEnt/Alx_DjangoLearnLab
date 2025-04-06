from rest_framework import viewsets,generics, permissions, serializers
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from datetime import date
from .permissions import IsOwnerOrReadOnly
from django.views.generic import ListView, UpdateView, DeleteView


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = '/books/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/books/'


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class AuthorViewSet(viewsets.ModelViewSet):
   
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value    
    
class BookListCreateView(generics.ListCreateAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    
class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # or 'pk'    
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'    
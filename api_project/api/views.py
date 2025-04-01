from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(viewsets.ListAPIView):
    queryset = Book.objects.all()  # Get all book entries from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data

from rest_framework import serializers
from .models import Book  # Import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model to be serialized
        fields = ['id', 'title', 'author']  # Include all fields you want in the response

from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
   
    
    def validate_publication_year(self, value):
        
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'  # Include all fields


class AuthorSerializer(serializers.ModelSerializer):
   
    books = BookSerializer(many=True, read_only=True)  # Nested books field

    class Meta:
        model = Author
        fields = ['name', 'books']

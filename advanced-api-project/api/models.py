from django.db import models

class Author(models.Model):
    
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name

class Book(models.Model):
   
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Relationship to Author

    def __str__(self):
        return self.title

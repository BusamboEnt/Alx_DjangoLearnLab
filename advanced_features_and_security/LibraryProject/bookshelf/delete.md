### Deleting a Book Instance in Django Shell

Run the following commands in the Django shell to delete the book you created:

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirming deletion by trying to retrieve the book again
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")

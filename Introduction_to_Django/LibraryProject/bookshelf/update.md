### Updating a Book Instance in Django Shell

Run the following commands in the Django shell to update the title of the book you created:

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Displaying the updated book title
print(book.title)

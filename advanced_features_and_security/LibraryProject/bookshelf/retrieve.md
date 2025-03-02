### Retrieving a Book Instance in Django Shell

Run the following command in the Django shell to retrieve the book you created:

```python
from bookshelf.models import Book

# Retrieving the book instance
book = Book.objects.get(title="1984")

# Displaying the book attributes
print(book.title, book.author, book.publication_year)

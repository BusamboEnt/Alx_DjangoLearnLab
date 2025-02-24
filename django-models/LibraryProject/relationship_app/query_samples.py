from relationship_app.models import Library

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the library by name
        books = library.books.all()  # Retrieve all books associated with the library
        return books
    except Library.DoesNotExist:
        return "Library not found."


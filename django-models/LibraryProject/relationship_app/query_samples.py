from relationship_app.models import Library, Author, Book, Librarian, Library

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the library by name
        books = library.books.all()  # Retrieve all books associated with the library
        return books
    except Library.DoesNotExist:
        return "Library not found."

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Get the author by name
        books = Book.objects.filter(author=author)  # Retrieve all books by this author
        return books
    except Author.DoesNotExist:
        return "Author not found."
    
    def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the library by name
        librarian = Librarian.objects.get(library=library)  # Retrieve the librarian for this library
        return librarian
    except Library.DoesNotExist:
        return "Library not found."
    except Librarian.DoesNotExist:
        return "No librarian assigned to this library."
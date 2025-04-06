"""
BookListCreateView:
- Supports GET and POST requests
- Allows filtering by title, author, and publication_year via query parameters
- Supports search on 'title' and 'author' fields
- Supports ordering by 'title' and 'publication_year'

Examples:
- /api/books/?author=Chinua Achebe
- /api/books/?search=Things
- /api/books/?ordering=-publication_year
"""
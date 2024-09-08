# README.md
## API Endpoints

- `GET /books/` - List all books with filtering, searching, and ordering capabilities
- `POST /books/` - Create a new book
- `GET /books/<int:pk>/` - Retrieve a book by ID
- `PUT /books/<int:pk>/` - Update a book by ID
- `DELETE /books/<int:pk>/` - Delete a book by ID

## Filtering, Searching, and Ordering

- Filter by title: `GET /books/?title=Harry`
- Filter by author name: `GET /books/?author__name=Rowling`
- Filter by publication year: `GET /books/?publication_year__gte=2000`
- Search by title or author name: `GET /books/?search=Harry`
- Order by title: `GET /books/?ordering=title`

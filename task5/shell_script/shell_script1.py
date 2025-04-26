from ..books.models import Book

books = Book.get_all_books()

for book in books:
     print(book)
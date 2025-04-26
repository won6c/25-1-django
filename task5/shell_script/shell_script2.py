from books.models import Book

all_books = Book.get_all_books()
print("📚전체 책 목록:")
for book in all_books:
    print(book)

orwell_books = Book.get_books_by_author("George Orwell")
print("\n🖋️George Orwell 책 목록 : ")
for book in orwell_books:
    print(book)

dystopia_books = Book.get_books_by_title_keyword("new")
print("\n🔍제목에 'new'가 포함된 책 목록")
for book in dystopia_books:
    print(book)

sorted_books = Book.get_books_ordered_by_title()
print("\n🔠제목 순 정렬 : ")
for book in sorted_books:
    print(book)
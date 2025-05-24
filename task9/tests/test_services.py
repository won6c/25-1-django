import pytest
from django.contrib.auth.models import User
from library.models import Book, BorrowHistory
from library.services.book_service import get_borrow_history_for_book
from library.exceptions import BookHasNoBorrowHistory

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():
    user = User.objects.create_user(username='testuser')  
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')  
    BorrowHistory.objects.create(book=book, user=user)  

    histories = get_borrow_history_for_book(book)  

    assert histories.count() == 1  
    assert histories.first().user == user  

@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():
    book = Book.objects.create(title='Empty Book', author='Nobody', isbn='9999999999999')  

    with pytest.raises(BookHasNoBorrowHistory) as exc_info:  
        get_borrow_history_for_book(book)  

    assert '도서에는 대출 이력이 없습니다.' in str(exc_info.value)

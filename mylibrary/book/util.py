from decimal import Decimal
from book.models import Book, Publisher


def create_book() -> None:
    Book.objects.create(price=Decimal('100.00'))

def create_book1() -> None:
    book = Book()
    book.price=Decimal('100.00')
    book.save()

def create_book2() -> None:
    Book.objects.create(price=('$', 10))

def create_book3() -> None:
    book = Book(price=('$', 10))

def create_book4() -> None:
    book = Book()
    book.price = ('$', 10)

def create_book5() -> None:
    book = Book.objects.create(author=None)

def create_book6() -> None:
    book = Book.objects.create(publisher=None)

def create_book7() -> None:
    publisher=Publisher.objects.get(name='Chilton Books')
    book = Book(author=publisher)

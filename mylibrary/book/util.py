from book.models import Book, Publisher


def create_book() -> None:
    Book.objects.create(price=('$', 10))

def create_book2() -> None:
    book = Book(price=('$', 10))

def create_book3() -> None:
    book = Book()
    book.price = ('$', 10)

def create_book4() -> None:
    book = Book(price=None)

def create_book5() -> None:
    book = Book(title=None)

def create_book6() -> None:
    publisher=Publisher.objects.get(name='Chilton Books')
    book = Book(author=publisher)

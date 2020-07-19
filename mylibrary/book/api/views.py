from rest_framework.viewsets import ModelViewSet

from book.api.serializers import (
    BookSerializer, AuthorSerializer,
    PublisherSerializer,
)
from book.models import Book, Author, Publisher


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from rest_framework.serializers import (
    ModelSerializer,
)
from book.models import Book, Author, Publisher


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

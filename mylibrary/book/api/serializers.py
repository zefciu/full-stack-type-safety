from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
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
        depth = 0
        fields = '__all__'

a_dict = {
        "France": "Paris",
        "Germany": "Berlin",
        "United States": "Washington D.C",
        "Spain": "Madrid",
}
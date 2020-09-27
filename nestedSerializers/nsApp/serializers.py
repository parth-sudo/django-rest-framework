from .models import Author,Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True) #nested serializer.
    #when the author info goes back, the books info go along it as well.
    #but read only. many=True means an array of JSON data of books.

    class Meta:
        model = Author
        fields = '__all__'

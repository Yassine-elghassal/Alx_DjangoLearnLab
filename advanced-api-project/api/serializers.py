from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > 2025:  # Current year for validation
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields from the Book model and includes custom validation for the 'publication_year' field.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure that the publication year is not in the future.
        """
        if value > 2025:  # Replace with the current year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Serializes the author's name and includes a nested BookSerializer to represent related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

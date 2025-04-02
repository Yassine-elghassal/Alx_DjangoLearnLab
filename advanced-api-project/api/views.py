from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ListView: To retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only for unauthenticated users

# DetailView: To retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only for unauthenticated users

# CreateView: To add a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a new book

# UpdateView: To modify an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

# DeleteView: To delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book

# BookListView: Allows both authenticated and unauthenticated users to retrieve a list of all books.
# Only authenticated users can create new books.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permission to allow read-only access for unauthenticated users

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# BookListView: Allows both authenticated and unauthenticated users to retrieve a list of all books.
# Only authenticated users can create new books.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permission to allow read-only access for unauthenticated users


# BookDetailView: Retrieve or update a specific book by its ID. Only authenticated users can update or delete books.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify or delete a book

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter  # Correct import
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

# Filter class to filter books by title, author, and publication_year
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Allows case-insensitive partial match for title
    author = filters.CharFilter(lookup_expr='icontains')  # Allows case-insensitive partial match for author
    publication_year = filters.NumberFilter()  # Filters by publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# BookListView: List and Create View for Book, includes filtering, search, and ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

    # Add filtering, searching, and ordering capabilities
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Correct filter backends
    filterset_class = BookFilter  # Apply the BookFilter class to handle the filtering logic
    search_fields = ['title', 'author']  # Allow searching by title and author
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication year
    ordering = ['title']  # Default ordering by title

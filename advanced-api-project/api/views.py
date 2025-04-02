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

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

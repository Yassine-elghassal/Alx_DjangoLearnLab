from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookTests(APITestCase):
    
    def setUp(self):
        """Set up test environment including a superuser and a regular user."""
        # Create a superuser and a regular user
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )

        # Create a Book instance for testing
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2021
        }
        self.book = Book.objects.create(**self.book_data)

        # Define the URL paths for testing
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book_authenticated(self):
        """Test the ability to create a book as an authenticated user."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.book_list_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_create_book_unauthenticated(self):
        """Test the ability to create a book as an unauthenticated user."""
        response = self.client.post(self.book_list_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test the ability to update a book as an authenticated user."""
        updated_data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "publication_year": 2022
        }
        self.client.login(username="testuser", password="testpassword")
        response = self.client.put(self.book_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_update_book_unauthenticated(self):
        """Test the ability to update a book as an unauthenticated user."""
        updated_data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "publication_year": 2022
        }
        response = self.client.put(self.book_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """Test the ability to delete a book as an authenticated user."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthenticated(self):
        """Test the ability to delete a book as an unauthenticated user."""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.book_list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        """Test searching books by author."""
        response = self.client.get(self.book_list_url, {'search': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_book_permissions(self):
        """Test permission settings to ensure only authorized users can modify books."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test as admin (superuser) can access all endpoints
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail
]

# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your custom views if needed

urlpatterns = [
    # Using Django's built-in LoginView
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Using Django's built-in LogoutView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Custom registration view
    path('register/', views.register, name='register'),
]

# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for adding and editing books
    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),  # URL for editing a book
]

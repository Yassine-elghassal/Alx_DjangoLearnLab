from django.shortcuts import render

# Create your views here.
# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library  # This line imports the Library model

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This will be used in the template

# relationship_app/views.py
from django.shortcuts import render
from relationship_app.models import Book

def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    
    # Render the list_books template and pass the books to it
    return render(request, 'relationship_app/list_books.html', {'books': books})
# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This will be used in the template


# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Library  # Import Library model

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This will be used in the template

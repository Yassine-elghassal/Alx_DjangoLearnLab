# query_samples.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian # type: ignore

def query_books_by_author(author_name):
    try:
        # Fetch the author by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by the author
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

def list_all_books_in_library(library_name):
    try:
        # Fetch the library by name
        library = Library.objects.get(name=library_name)
        
        # Get all books in the library (ManyToMany relationship)
        books = library.books.all()
        
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

def retrieve_librarian_for_library(library_name):
    try:
        # Fetch the library by name
        library = Library.objects.get(name=library_name)
        
        # Get the librarian for the library (OneToOne relationship)
        librarian = Librarian.objects.get(library=library)
        
        print(f"Librarian for the library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned for the library '{library_name}'")

if __name__ == "__main__":
    # Example queries
    query_books_by_author("J.K. Rowling")
    list_all_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")

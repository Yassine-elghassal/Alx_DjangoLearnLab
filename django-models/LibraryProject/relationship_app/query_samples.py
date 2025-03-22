import os
import django

# Set the settings module before calling django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example Usage
if __name__ == "__main__":
    print(list(books_by_author("J.K. Rowling")))
    print(list(books_in_library("Central Library")))
    print(librarian_of_library("Central Library"))

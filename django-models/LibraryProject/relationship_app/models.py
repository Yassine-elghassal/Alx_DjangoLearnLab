# relationship_app/models.py
from django.db import models

# Author model: This will store author names
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model: This will store book titles, linked to an author through ForeignKey
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# Library model: This will store library names and their associated books (ManyToMany relationship)
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# Librarian model: This will store librarian names, each assigned to a specific library (OneToOne relationship)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

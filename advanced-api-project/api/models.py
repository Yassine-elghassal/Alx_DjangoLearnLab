from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    """
    Author model to store information about authors.
    The 'name' field represents the author's full name.
    """
    name = models.CharField(max_length=100)

class Book(models.Model):
    """
    Book model to store information about books.
    The 'title' is the name of the book, and the 'publication_year' stores the year the book was published.
    The 'author' field is a ForeignKey to the Author model, establishing a one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

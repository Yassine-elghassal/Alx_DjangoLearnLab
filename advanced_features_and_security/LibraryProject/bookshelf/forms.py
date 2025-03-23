# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book  # Import your model, or any other model you want to use

class ExampleForm(forms.Form):
    # Example of a form field
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    publish_date = forms.DateField()

    # You can add more fields depending on your needs

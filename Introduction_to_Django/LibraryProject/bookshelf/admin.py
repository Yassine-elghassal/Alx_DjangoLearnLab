from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

admin.site.register(Book)
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Show these fields in the list view
    list_filter = ("publication_year", "author")  # Enable filtering by year and author
    search_fields = ("title", "author")  # Allow searching by title and author

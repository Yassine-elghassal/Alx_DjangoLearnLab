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

# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin View - Only accessible by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View - Only accessible by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View - Only accessible by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to add a book (only users with 'can_add_book' permission can access)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')  # Assuming you are passing author ID
        Book.objects.create(title=title, author_id=author)
        return redirect('book_list')  # Redirect to a page that lists books
    return render(request, 'relationship_app/add_book.html')

# View to edit a book (only users with 'can_change_book' permission can access)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')  # Assuming you are passing author ID
        book.save()
        return redirect('book_list')  # Redirect to a page that lists books
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to delete a book (only users with 'can_delete_book' permission can access)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')  # Redirect to a page that lists books

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm defined

# Add Book View
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')  # Redirect to the same page or a different one after saving
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

# Edit Book View
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('edit_book', id=book.id)  # Redirect to the same page or another after saving
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

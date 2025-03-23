from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import LogEntry
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Define the list display for the user admin page
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    # Define the fields to be displayed in the form when creating/editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Define the fields to be displayed in the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add the custom manager to the admin interface
    add_form = CustomUser

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(LogEntry)

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    
# Create the groups and assign permissions manually through the admin interface or use a data migration
def create_groups():
    # Admin group
    admin_group, created = Group.objects.get_or_create(name='Admins')
    admin_group.permissions.add(*Book._meta.permissions)  # Assign all permissions

    # Editors group
    editors_group, created = Group.objects.get_or_create(name='Editors')
    editors_group.permissions.add('can_create', 'can_edit')

    # Viewers group
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    viewers_group.permissions.add('can_view')

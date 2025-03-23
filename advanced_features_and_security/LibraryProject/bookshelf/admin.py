from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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

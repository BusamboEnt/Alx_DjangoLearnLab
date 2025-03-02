from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    search_fields = ('title', 'author')  
    list_filter = ('publication_year',)  

from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff", "date_of_birth")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff"),
        }),
    )
    ordering = ("email",)
    search_fields = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

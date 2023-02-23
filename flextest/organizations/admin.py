from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields":("first_name", "last_name", "icon","organizations")}),
        ("Contacts", {"fields":("phone",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email","first_name", "last_name", "icon","phone", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ['id', 'name']

admin.site.register(User, CustomUserAdmin)

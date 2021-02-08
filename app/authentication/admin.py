from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User


class UserAdmin(BaseUserAdmin):
    """ Improves the settings displayed in the admin panel"""
    ordering = ['id']
    list_display = ['email', 'title', 'first_name', 'last_name', 'auth_provider', 'created_at', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('title', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

# Register your models here.
class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username','cpf','telephone')
    list_filter = ('email', 'username','cpf','telephone' ,'is_active', 'is_staff')
    ordering = ('-telephone',)
    list_display = ('email','id', 'username','cpf','telephone',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username','cpf','telephone' )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name','cpf','telephone', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)

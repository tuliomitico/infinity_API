from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Store)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id','slug')
    prepopulated_fields = {'slug': ('name',),}
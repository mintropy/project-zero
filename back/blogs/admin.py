from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Blog, BlogPost

# Register your models here.
@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ("id", "name", "user")
    pass

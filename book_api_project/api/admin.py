# api/admin.py
from django.contrib import admin
from .models import Book, Publisher

admin.site.register(Book)
admin.site.register(Publisher)
from django.contrib import admin
from .models import Post, Author, Book, City

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(City)

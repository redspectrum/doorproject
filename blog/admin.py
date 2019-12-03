from django.contrib import admin
from .models import Post, Author, Book, City

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')



# Register your models here.
admin.site.register(Post)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(City)

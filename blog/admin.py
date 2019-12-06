from django.contrib import admin
from .models import Post, Author, Book, City, Task, Letter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('url', 'published')


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'email_destination', 'body', 'sending_time')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_book', 'price')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name_city', 'author_city')


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(City, CityAdmin)

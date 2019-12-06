from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавие')
    author_book = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='author_book')
    price = models.IntegerField(verbose_name='Цена')


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавие поста')
    body = models.TextField(blank=True, db_index=True, verbose_name='Тело поста')
    author_posts = models.ManyToManyField(Author, verbose_name='author_posts')

    def __str__(self):
        return self.title

class City(models.Model):
    name_city = models.CharField(max_length=50, verbose_name='Город')
    author_city = models.OneToOneField(Author, on_delete=models.CASCADE, verbose_name='author_city')

    def __str__(self):
        return self.name_city

class Task(models.Model):

    url = models.CharField(max_length=50, verbose_name='Ссылка')
    published = models.DateTimeField(verbose_name='Время поста')

    def __str__(self):
        return self.url

class Letter(models.Model):

    title = models.CharField(max_length=50, blank=True, verbose_name='Заглавие письма')
    email_destination = models.EmailField(blank=True, verbose_name='Email получателя')
    body = models.TextField(blank=True, db_index=True, verbose_name='Тело письма')
    sending_time = models.DateTimeField(verbose_name='Время отправки', blank=True)

    def __str__(self):
        return self.title
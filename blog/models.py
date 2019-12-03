from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author_book = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, db_index=True)
    author_posts = models.ManyToManyField(Author)


class City(models.Model):
    name_city = models.CharField(max_length=50)
    author_city = models.OneToOneField(Author, on_delete=models.CASCADE)
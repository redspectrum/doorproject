# Generated by Django 2.2.7 on 2019-12-05 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191202_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50, verbose_name='Ссылка')),
                ('published', models.DateTimeField(verbose_name='Время поста')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author', verbose_name='author_book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заглавие'),
        ),
        migrations.AlterField(
            model_name='city',
            name='author_city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Author', verbose_name='author_city'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_posts',
            field=models.ManyToManyField(to='blog.Author', verbose_name='author_posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, db_index=True, verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заглавие поста'),
        ),
    ]
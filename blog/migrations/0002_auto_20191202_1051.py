# Generated by Django 2.2.7 on 2019-12-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]

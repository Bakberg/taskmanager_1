# Generated by Django 3.2.6 on 2021-09-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('glav', '0007_auto_20210903_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dropdown_for',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(blank=True, verbose_name='Описание')),
                ('datab', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('datas', models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фотография')),
                ('is_pblished', models.BooleanField(default=True, verbose_name='Публирован')),
                ('book', models.FileField(blank=True, upload_to='static/%Y/%m/%d', verbose_name='PDF книги')),
            ],
            options={
                'verbose_name': 'Инновация категорий',
                'verbose_name_plural': 'Инновация категорий',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(blank=True, verbose_name='Описание')),
                ('datab', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('datas', models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фотография')),
                ('is_pblished', models.BooleanField(default=True, verbose_name='Публирован')),
                ('book', models.FileField(blank=True, upload_to='static/%Y/%m/%d', verbose_name='PDF книги')),
            ],
            options={
                'verbose_name': 'Образование категорий',
                'verbose_name_plural': 'Образование категорий',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(blank=True, verbose_name='Описание')),
                ('datab', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('datas', models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фотография')),
                ('is_pblished', models.BooleanField(default=True, verbose_name='Публирован')),
                ('book', models.FileField(blank=True, upload_to='static/%Y/%m/%d', verbose_name='PDF книги')),
            ],
            options={
                'verbose_name': 'Методология категорий',
                'verbose_name_plural': 'Методология категорий',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(blank=True, verbose_name='Описание')),
                ('datab', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('datas', models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фотография')),
                ('is_pblished', models.BooleanField(default=True, verbose_name='Публирован')),
                ('book', models.FileField(blank=True, upload_to='static/%Y/%m/%d', verbose_name='PDF книги')),
            ],
            options={
                'verbose_name': 'Наука категорий',
                'verbose_name_plural': 'Наука категорий',
            },
        ),
    ]
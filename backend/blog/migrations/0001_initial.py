# Generated by Django 3.0.2 on 2020-01-20 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(default=None, max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(default=None, max_length=15, unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('contact_number', models.CharField(max_length=20, verbose_name='Contact Number')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='avatar')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=100)),
                ('recipe_ingredient', models.TextField()),
                ('recipe_timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipe_image', models.ImageField(upload_to='')),
                ('recipe_duration', models.CharField(default=None, max_length=20)),
                ('recipe_serving', models.CharField(default=None, max_length=20)),
                ('recipe_description', models.TextField(default=None)),
                ('recipe_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipe_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'Recipes',
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('recipe_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='blog.Recipe')),
            ],
        ),
    ]

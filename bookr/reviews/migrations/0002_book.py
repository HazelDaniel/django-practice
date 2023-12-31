# Generated by Django 5.0 on 2023-12-31 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of the book', max_length=70)),
                ('publication_date', models.DateField(verbose_name='Date the book was published')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number of the book')),
            ],
        ),
    ]

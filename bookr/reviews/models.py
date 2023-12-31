from django.db import models

# Create your models here.


class Publisher(models.Model):
    """the class representation of the publisher table"""
    name = models.CharField(help_text="this is the name of the publisher", max_length=50)
    website = models.URLField(help_text="this is the website of the publisher")
    email = models.EmailField(help_text="this is the publisher's email address", max_length=20)

class Book(models.Model):
    """the class representation of the book table"""
    title = models.CharField(max_length=70, help_text="title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
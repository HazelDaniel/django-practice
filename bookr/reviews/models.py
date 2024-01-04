from django.db import models
from django.contrib import auth

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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

class Contributor(models.Model):
    """the class representation of the contributor table"""
    first_names = models.CharField(max_length=50, help_text="The contributor's first name(s)")
    last_names = models.CharField(max_length=50, help_text="The contributor's last name(s)")
    email = models.EmailField(help_text="The contributor's contact email")

class BookContributor(models.Model):
    """the class representation of the many-to-many relationship
        between the book table and the contributor table"""
    class ContributorRoles(models.TextChoices):
        """a class representation of the enumerated list of choices
            for the contributor roles"""
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="the role of the contributor",
                            choices=ContributorRoles.choices, max_length=20)

class Review(models.Model):
    """the class representation of the review table"""
    content = models.TextField(help_text="Review text")
    rating = models.IntegerField(help_text="The rating score")
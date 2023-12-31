from django.db import models

# Create your models here.


class Publisher(models.Model):
    """ths class representation of the publisher table"""
    name = models.CharField(help_text="this is the name of the publisher", max_length=50)
    website = models.URLField(help_text="this is the website of the publisher")
    email = models.EmailField(help_text="this is the publisher's email address", max_length=20)

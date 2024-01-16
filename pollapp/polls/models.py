#!/usr/bin/env python3
# Create your models here.
from django.db import models
from datetime import datetime
from django.utils import timezone


class Question(models.Model):
    """this is the model for the question table"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(help_text="date published", verbose_name="the date the question was published")

    def was_published_recently(self):
        """this returns whether the
            question was recently published"""
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        """the string evaluation of this class"""
        return f"{self.question_text}"


class Choice(models.Model):
    """this is the model for the choice table"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """the string evaluation of this class"""
        return f"{self.choice_text}"

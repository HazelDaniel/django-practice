# Generated by Django 5.0 on 2024-01-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_contributor_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-24 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_remove_books_user_booksloaned'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksloaned',
            name='date_loan',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 21, 9, 50, 415439)),
        ),
    ]

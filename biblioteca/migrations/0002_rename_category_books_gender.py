# Generated by Django 4.2.6 on 2023-10-26 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='category',
            new_name='gender',
        ),
    ]

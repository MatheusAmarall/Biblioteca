from django.db import models
from django.contrib.auth.models import User

class Genres(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genres'

class Books(models.Model):
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Genres, on_delete=models.CASCADE)
    qtdPages = models.IntegerField()
    bookCover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    qtdBooks = models.IntegerField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class BooksLoaned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book
    
    class Meta:
        verbose_name = 'BookLoaned'
        verbose_name_plural = 'BooksLoaned'

from django.db import models

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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

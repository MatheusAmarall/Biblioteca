from django.contrib import admin
from .models import Books, Genres, BooksLoaned

admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(BooksLoaned)
from django.shortcuts import render, redirect
from .models import Books, Genres

def index(request):
    livros = Books.objects.all()

    return render(request, 'pages/index.html', {'livros':livros})

def add_book(request):

    if request.method == 'POST':
        pass
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        bookCover = request.FILES.get('bookCover')
        qtdPages = request.POST.get('qtdPages')
        qtdBooks = request.POST.get('qtdBooks')
        author = request.POST.get('author')

        Books.objects.create(
            name=name,
            gender_id=gender,
            bookCover=bookCover,
            qtdPages=qtdPages,
            author=author,
            qtdBooks=qtdBooks
        )

        return redirect('home')
    else:
        generos = Genres.objects.all()
        return render(request, 'pages/add-book.html', {'generos':generos})

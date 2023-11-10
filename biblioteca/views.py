from django.shortcuts import render, redirect
from .models import Books, Genres
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(redirect_field_name='login')
def index(request):
    livros = Books.objects.all()
    return render(request, 'pages/index.html', {'livros':livros})

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def add_book(request):

    if request.method == 'POST':
        pass
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        bookCover = request.FILES.get('bookCover')
        qtdPages = request.POST.get('qtdPages')
        qtdBooks = request.POST.get('qtdBooks')
        author = request.POST.get('author')
        in_stock = int(request.POST.get('qtdBooks')) > 0

        Books.objects.create(
            name=name,
            gender_id=gender,
            bookCover=bookCover,
            qtdPages=qtdPages,
            author=author,
            qtdBooks=qtdBooks,
            in_stock=in_stock
        )

        return redirect('home')
    else:
        generos = Genres.objects.all()
        return render(request, 'pages/add-book.html', {'generos':generos})
    
def loan_book(request, id):
    book = Books.objects.get(id=id)
    book.qtdBooks -= 1
    
    if book.qtdBooks == 0:
        book.in_stock = False
    
    book.save()
    return redirect('home')

from django.shortcuts import render, redirect
from .models import Books, Genres, BooksLoaned
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .utils import send_email
from datetime import datetime

@login_required(redirect_field_name='login')
def index(request):
    livros = Books.objects.all()
    return render(request, 'pages/index.html', {'livros':livros})

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def add_book(request):

    if request.method == 'POST':
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
    BooksLoaned.objects.create(
        user_id=request.user.id,
        book_id=id
    )

    # send_email("Empréstimo de livro", f"Você pegou o livro {book.name} emprestado no dia de hoje: {datetime.now()}", request.user.email)
    
    if book.qtdBooks == 0:
        book.in_stock = False
    
    book.save()
    return redirect('home')


def loan_books(request):
    if not request.user.is_superuser:
        livrosEmprestados = BooksLoaned.objects.filter(user_id=request.user.id, returned=False)
        livros = []
        for livroEmprestado in livrosEmprestados:
            livros.append(livroEmprestado.book)
        
        return render(request, 'pages/loan-books.html', {'livros':livros})
    
    return redirect('home')

def return_book(request, id):
    loaned_books = BooksLoaned.objects.filter(user_id=request.user.id, book_id=id)
    loaned_books[0].delete()
    book = Books.objects.get(id=id)
    if not book.in_stock:
        book.in_stock = True
    book.qtdBooks += 1
    book.save()
    
    return redirect('home') if len(loaned_books) == 0 else redirect('loan-books')
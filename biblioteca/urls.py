from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('loan-books/', views.loan_books, name='loan-books'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('loan-book/<int:id>', views.loan_book, name='loan-book'),
    path('return-book/<int:id>', views.return_book, name='return-book')
]
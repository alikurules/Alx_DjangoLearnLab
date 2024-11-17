from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # URL for the book list
    path('books/<int:book_id>/', views.books, name='books'),  # URL for book details
]

from django.urls import path
from .views import list_books, LibraryDetailView, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]

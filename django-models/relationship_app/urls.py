from django.urls import path
from .views import LibraryDetailView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail
]

from django.urls import path
from .views import LibraryDetailView, CustomLoginView, CustomLogoutView, RegisterView
from . import views
from .views import list_books

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail
]




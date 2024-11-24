from django.shortcuts import render
from rest_framework.viewsets import viewsets.ModelViewSet
from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
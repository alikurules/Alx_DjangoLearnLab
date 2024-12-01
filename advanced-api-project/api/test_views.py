from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.list_url = reverse('book-list')  # Update with your URL name
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

# Create a book
def test_create_book(self):
    data = {
        "title": "Harry Potter and the Chamber of Secrets",
        "publication_year": 1998,
        "author": self.author.id
    }
    response = self.client.post(self.list_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)

# Retrieve a book
def test_get_book(self):
    response = self.client.get(self.detail_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], self.book.title)

# Update a book
def test_update_book(self):
    data = {"title": "Harry Potter Updated"}
    response = self.client.patch(self.detail_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, "Harry Potter Updated")

# Delete a book
def test_delete_book(self):
    response = self.client.delete(self.detail_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)
    
# Filter by title
def test_filter_books_by_title(self):
    response = self.client.get(f"{self.list_url}?title=Harry Potter")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

# Search by author name
def test_search_books_by_author(self):
    response = self.client.get(f"{self.list_url}?search=Rowling")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

# Order by publication_year
def test_order_books_by_publication_year(self):
    response = self.client.get(f"{self.list_url}?ordering=-publication_year")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['publication_year'], self.book.publication_year)
    
from rest_framework.test import APIClient

def test_unauthenticated_user_cannot_create_book(self):
    client = APIClient()  # Unauthenticated client
    data = {
        "title": "Unauthorized Book",
        "publication_year": 2020,
        "author": self.author.id
    }
    response = client.post(self.list_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author
from datetime import date
from django.test import TestCase


class BookAPITestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Author A')  # create an Author instance

        self.book1 = Book.objects.create(
            title='Book One',
            author=self.author,  # assign the Author instance
            published_date=date(2020, 1, 1)
        )
        self.book2 = Book.objects.create(
            title='Book Two',
            author=self.author,
            published_date=date(2021, 2, 2)
        )

def test_update_book(self):
    url = reverse('book-detail', kwargs={'pk': self.book1.pk})
    data = {
        'title': 'Updated Title',
        'author': self.author1.id,
        'published_date': '2020-01-01'
    }
    response = self.client.put(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_create_book(self):
    data = {
        'title': 'New Book',
        'author': self.author1.id,  # Use ID, not name
        'published_date': '2023-03-15'
    }
    response = self.client.post(self.book_create_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass123')
    self.client = APIClient()
    self.client.login(username='testuser', password='testpass123')

    # Create Author instances first
    self.author1 = Author.objects.create(name='Author A')
    self.author2 = Author.objects.create(name='Author B')

    # Now assign author as a ForeignKey instance
    self.book1 = Book.objects.create(title='Book One', author=self.author1, published_date=date(2020, 1, 1))
    self.book2 = Book.objects.create(title='Book Two', author=self.author2, published_date=date(2021, 2, 2))

    self.book_create_url = reverse('book-list')  # adjust this to match your router/view name


def test_unauthenticated_create_book(self):
    self.client.logout()
    data = {'title': 'Unauthorized Book', 'author': 'Author X', 'published_date': '2022-01-01'}
    response = self.client.post(self.book_create_url, data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass123')

        self.book1 = Book.objects.create(title='Book One', author='Author A', published_date=date(2020, 1, 1))
        self.book2 = Book.objects.create(title='Book Two', author='Author B', published_date=date(2021, 2, 2))
        self.book_create_url = reverse('book-list')  # Adjust to your URL name

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'Author Z',
            'published_date': '2023-03-15'
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_get_book_list(self):
        response = self.client.get(self.book_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})  # Adjust to your URL name
        data = {'title': 'Updated Title', 'author': 'Author A', 'published_date': '2020-01-01'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.book_create_url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books_by_title(self):
        response = self.client.get(self.book_create_url, {'search': 'One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('Book One', response.data[0]['title'])

    def test_order_books_by_title(self):
        response = self.client.get(self.book_create_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(response.data[0]['title'], response.data[1]['title'])
        
        

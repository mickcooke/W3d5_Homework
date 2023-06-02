import unittest

from models.book import Book
from models.books import *

class TestBook(unittest.TestCase):

    def setUp(self):
        # self.book = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Childrens", "Bloomsbury", "Harry Potter is a wizard. He is in his second year at Hogwarts School of Witchcraft and Wizardry. Little does he know that this year will be just as eventful as the last...", True)
        self.book1 = book1
        self.book2 = book2
        self.book3 = Book("Incognito", "David Eagleman", "Popular Science", "Cannongate", "Renowned neuroscientist David Eagleman navigates the depths of the subconscious brain to illuminate surprising mysteries", False)
        

    def test_book_has_title(self):
        self.assertEqual("Harry Potter and the Chamber of Secrets", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("J.K. Rowling", self.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Childrens", self.book1.genre)

    def test_book_has_publisher(self):
        self.assertEqual("Bloomsbury", self.book1.publisher)        

    def test_book_has_description(self):
        self.assertEqual("Harry Potter is a wizard. He is in his second year at Hogwarts School of Witchcraft and Wizardry. Little does he know that this year will be just as eventful as the last...", self.book1.description)       

    def test_book_has_checked_out_status(self):
        self.assertEqual(True, self.book1.checked_out)  

    def test_library_has_books(self):
        self.books = books
        self.result = len(books)
        self.assertEqual(2, self.result)  

    def test_add_new_book(self):
        self.books = books
        add_new_book(self.book3)
        self.result = len(books)
        self.assertEqual(3, self.result)  

    def test_delete_book(self):
        self.books = books
        delete_book(0)
        self.result = self.books[0].title
        self.assertEqual("Conversations with McCartney", self.result)


    
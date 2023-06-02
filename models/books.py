from models.book import *

book1 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Childrens", "Bloomsbury", "Harry Potter is a wizard. He is in his second year at Hogwarts School of Witchcraft and Wizardry. Little does he know that this year will be just as eventful as the last...", True)

book2 = Book("Conversations with McCartney", "Paul Du Noyer", "Biography", "Hodder & Stoughton", "McCartney on McCartney is the culmination of Du Noyer's long association with McCartney and his music. It draws from their interview sessions across 35 years, coupling McCartney's own, candid thoughts with his observations and analysis.", False)

books = [book1, book2]

def add_new_book(book):
    books.append(book)

def delete_book(index):
    books.pop(index)

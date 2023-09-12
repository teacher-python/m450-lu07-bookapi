import json

from flask import current_app

from book import Book


class BookDAO:
    def __init__(self):
        self._bookdict = {}
        self.load_books()

    def list_books(self):
        return self._bookdict

    def read_book(self, book_uuid):
        if book_uuid in self._bookdict:
            return self._bookdict[book_uuid]
        return None

    def load_books(self):
        file = open(current_app.config['DATAPATH'] + 'books.json', encoding='UTF-8')
        books = json.load(file)
        for item in books:
            key = item['bookUUID']
            book = Book(
                item['bookUUID'],
                item['title'],
                item['author'],
                item['price'],
                item['format'],
                item['isbn']
            )
            self._bookdict[key] = book

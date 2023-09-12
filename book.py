from dataclasses import dataclass


@dataclass
class Book(dict):
    book_uuid: str
    title: str
    author: str
    price: float
    format: str
    isbn: str = ''

    def to_json(self):
        jstring = f'"book_uuid": "{self.book_uuid}",' \
                  f'"title": "{self.title}",' \
                  f'"author": "{self.author}",' \
                  f'"price": {self.price},' \
                  f'"format": "{self.format}",' \
                  f'"isbn": "{self.isbn}"'
        return '{' + jstring + '}'

    @property
    def book_uuid(self):
        return self._book_uuid

    @book_uuid.setter
    def book_uuid(self, value):
        self._book_uuid = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

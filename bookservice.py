from flask import make_response
from flask_restful import Resource, reqparse

from bookdao import BookDAO


class BookService(Resource):
    def __init__(self):
        """
        constructor

        Parameters:

        """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('book_uuid', location='form', default=None, help='valid uuid')
        self.parser.add_argument('title', location='form', default=None, help='book title')
        self.parser.add_argument('author', location='form', default=None, help='authors name')
        self.parser.add_argument('price', location='form', default=None, help='price')
        self.parser.add_argument('isbn', location='form', default=None, help='isbn-13')
        self.parser.add_argument('format', location='form', default=None, help='format')

    def get(self, book_uuid):
        book_dao = BookDAO()
        book = book_dao.read_book(book_uuid)
        if book is not None:
            http_status = 200
            data = book.to_json()
        else:
            data = ''
            http_status = 404

        return make_response(data, http_status)

    def delete(self, book_uuid):
        pass

    def post(self):
        args = self.parser.parse_args()

    def put(self):
        args = self.parser.parse_args()

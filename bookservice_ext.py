import uuid
import re

from flask import make_response
from flask_restful import Resource, reqparse

from authorization import token_required, admin_required
from bookdao import BookDAO


class BookServiceExt(Resource):
    def __init__(self):
        """
        constructor

        Parameters:

        """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('book_uuid', location='form', default=None, help='valid uuid')
        self.parser.add_argument('title', location='form', required=True, default=None, help='book title')
        self.parser.add_argument('author', location='form', required=True, default=None, help='authors name')
        self.parser.add_argument('price', location='form', required=True, type=float, default=None, help='price')
        self.parser.add_argument('isbn', location='form', default='', help='isbn-13')
        self.parser.add_argument('format', location='form', required=True, default=None, help='format')

    @token_required
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

    @token_required
    @admin_required
    def delete(self, book_uuid):
        book_dao = BookDAO()
        book = book_dao.read_book(book_uuid)
        if book is not None:
            http_status = 200
        else:
            http_status = 404

        return make_response('', http_status)

    @token_required
    @admin_required
    def post(self):
        args = self.parser.parse_args()
        if args.book_uuid is None or args.book_uuid == '':
            args.book_uuid = str(uuid.uuid4())

        if not self.validate(args):
            http_status = 422
        else:
            book_dao = BookDAO()
            book = book_dao.read_book(args.book_uuid)
            if book is not None:
                http_status = 200
            else:
                http_status = 201

        return make_response('', http_status)

    def validate(self, args):
        if not re.match(
                '^[\x20-\x7E\xA0-\xA3\xA5\xA7\xA9-\xB3\xB5-\xB7\xB9-\xBB\xBF-\xFF\u20AC\u0160\u0161\u017D\u017E\u0152\u0153\u0178]{2,50}$',
                args.title
        ):
            return False
        if not re.match(
                '^[\x20-\x7E\xA0-\xA3\xA5\xA7\xA9-\xB3\xB5-\xB7\xB9-\xBB\xBF-\xFF\u20AC\u0160\u0161\u017D\u017E\u0152\u0153\u0178]{4,100}$',
                args.author
        ):
            return False
        if not re.match(r'^(?:-13)?:?\x20*(?=.{17}$)97(?:8|9)([ -])\d{1,5}\1\d{1,7}\1\d{1,6}\1\d$', args.isbn):
            return False
        if args.format not in ['Hardcover', 'Softcover', 'eBook', 'Audio']:
            return False

        try:
            price = float(args.price)
            if 300.00 <= price <= 0.00:
                return False
        except ValueError:
            return False
        return True

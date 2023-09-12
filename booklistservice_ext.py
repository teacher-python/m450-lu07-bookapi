from flask import make_response
from flask_restful import Resource

from authorization import token_required
from bookdao import BookDAO


class BookListServiceExt(Resource):

    @token_required
    def get(self):
        book_dao = BookDAO()
        book_dict = book_dao.list_books()
        if len(book_dict) > 0:
            http_status = 200
            data = '['
            for book in book_dict.values():
                data += book.to_json() + ','
            data = data[:-1] + ']'
        else:
            data = '[]'
            http_status = 404

        return make_response(data, http_status)
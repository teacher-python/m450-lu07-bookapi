from flask import Flask

from flask_cors import CORS
from flask_restful import Api

from authenticationservice import AuthenticationService
from booklistservice import BookListService
from booklistservice_ext import BookListServiceExt
from bookservice import BookService
from bookservice_ext import BookServiceExt

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('./.env')
api = Api(app)
api.add_resource(BookService, '/read/<book_uuid>', '/save', '/delete/<book_uuid>')
api.add_resource(BookServiceExt, '/ext/read/<book_uuid>', '/ext/save')
api.add_resource(BookListService, '/list')
api.add_resource(BookListServiceExt, '/ext/list')
api.add_resource(AuthenticationService, '/ext/login')

if __name__ == '__main__':
    app.run()

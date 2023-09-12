from flask import Flask

from flask_cors import CORS
from flask_restful import Api

from booklistservice import BookListService
from bookservice import BookService

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('./.env')
api = Api(app)
api.add_resource(BookService, '/read/<book_uuid>')
api.add_resource(BookListService, '/list')

if __name__ == '__main__':
    app.run()

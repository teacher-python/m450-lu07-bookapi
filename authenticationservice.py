from flask import make_response
from flask_restful import Resource, reqparse

from authorization import make_access_token


class AuthenticationService(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', location='form', help='username')
        self.parser.add_argument('password', location='form', help='password')

    def post(self):
        args = self.parser.parse_args()
        if args.username == 'admin' and args.password == 'admin':
            role = 'admin'
            http_statuscode = 200
        elif args.username == 'musterh' and args.password == 'geheim':
            role = 'user'
            http_statuscode = 200
        else:
            role = 'guest'
            http_statuscode = 401
        token = make_access_token(role)
        return make_response(token, http_statuscode)

from datetime import datetime, timedelta
from functools import wraps
import jwt
from flask import jsonify, request, make_response, g, current_app


def token_required(func):
    """
    checks if the authorization token is valid
    :param func: callback function
    :return:
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
            data = jwt.decode(token[7:], current_app.config['ACCESS_TOKEN_KEY'], algorithms=["HS256"])
            g.role = data['role']
        except Exception:
            return make_response(jsonify({"message": "EXAM/auth: Invalid token!"}), 401)

        return func(*args, **kwargs)

    return decorator


def admin_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if not g.role == 'admin':
            return make_response(jsonify({"message": "admin required"}), 403)
        return func(*args, **kwargs)

    return wrap


def make_access_token(role):
    """
    creates an access token
    :param role: the role of this user
    :return: token
    """

    access = jwt.encode({
        'role': role,
        'exp': datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_DURATION'])
    },
        current_app.config['ACCESS_TOKEN_KEY'], "HS256"
    )
    return access

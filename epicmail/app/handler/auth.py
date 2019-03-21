import jwt
import datetime
from functools import wraps
from epicmail.app import app
from flask import Flask, jsonify, request, json

sec_key = app.config.get('SECRET_KEY')

class JwtAuth:
    def encode_token(self, user_id):
        token = jwt.encode({'email': user_id,
                            'exp': datetime.datetime.utcnow(
                            ) + datetime.timedelta(minutes=2)},
                           sec_key)
        return token.decode('utf-8')

    def user_token(self, f):
        @wraps(f)
        def _verify(*args, **kwargs):
            auth_headers = request.headers.get('Authorization', '').split()
            try:
                token = auth_headers[1]
                print(token)
                if not token:
                    error = jsonify({'message': 'Token is missing'}), 403
                data = jwt.decode(token, sec_key)
                return f(*args, **kwargs)
            except IndexError:
                error = jsonify({
                    "message": "Token does not exist",
                    "authenticated": False
                }), 401
            except jwt.DecodeError:
                error = jsonify({
                    "message": "Token Decode Failed!",
                    "authenticated": False
                }), 401
            except jwt.ExpiredSignatureError:
                error = jsonify({
                    'message': 'Expired token. Please Log In again.',
                    'authenticated': False
                }), 401
            except jwt.InvalidTokenError:
                error = jsonify({
                    'message': 'Invalid token. Please Log In again',
                    'authenticated': False
                }), 401
            return error

        return _verify


    def get_token_from_header(self):
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or "Bearer" not in authorization_header:
            return jsonify({
                "error": "Bad authorization header",
                "status": 400
            })
        token = authorization_header.split(" ")[1]
        return token

    def decode_token(self, token):
        decoded = jwt.decode(token, sec_key, algorithms="HS256")
        return decoded['user_id']

import jwt
import datetime
from functools import wraps
from flask import jsonify, request


class Authentication:
    """Class for JWT"""
    def encode_token(self, id):
        """Creates the token"""
        token = jwt.encode(
            {
                'user_id': id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                
            },
        'sdfghjk,l.'
        )
        return token.encode('utf-8')
    
    def decode_token(self, token):
        """Breaks down the created token"""
        decode = jwt.decode(token, 'sdfghjk,l.', algorithms="HS256")
        return decode['id']

    def extracted_token(self):
        """Gets the token from the header to be decoded to the user id"""
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or "Bearer" not in authorization_header:
            return jsonify({
                "status": 400,
                "error": "Bad authorization header"
            })
        token = authorization_header.split(" ")[1]
        return token

    def token_required(self, f):
        """Decorator to enforse token authorization per endpoint"""
        @wraps(f)
        def tokenizer(*args, **kwargs):
            auth_headers =  request.headers.get("Authorization", "").split()
            try:
                token = auth_headers[1]
                print(token)
                if not token:
                    error = jsonify({
                        "status": 403,
                        "message": "Token not submitted"
                    }), 403
                data=jwt.decode(token, "sdfghjk,l.")
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

            return error
        return tokenizer
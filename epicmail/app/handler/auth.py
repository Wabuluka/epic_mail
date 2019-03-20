import jwt
import datetime

from functools import wraps
from flask import jsonify, request, make_response
from epicmail.app.models.users import User, users


def tok_req(func):
    @wraps(func)    
    def decorated(*args, **kwargs):
        token = None

        if 'auth_token' in request.headers:
            token = request.headers['auth_token']

        if not token:
            responseObject = {
                "status": 400,
                "error": "Token is missing"
            }
            return make_response(jsonify(responseObject)), 400
        try:
            user_id = User.decode_auth_token(token)
            current_user = user_id

            if not isinstance(current_user, int):
                responseObject = {
                    "message": current_user
                }
                return make_response(jsonify(responseObject))

            

# empicmail/app/models.py
import datetime
import jwt

from flask import jsonify
from epicmail.app import app, bcrypt
"""
All the models of the API and the relevant valis=dations are defined
"""

users = []

class User:
    """User Model contains the properties stored for a user"""

    

    def __init__(self, user_id, email, firstname, lastname, password_hash):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(
            password_hash, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()

    def to_dictionary(self):
        return {
            "id":self.user_id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "password":self.password_hash,
            "registered_on":self.registered_on
        }
    
    # jwt token generator
    def encode_auth_token(self, user_id):
        """Encode Tokens"""
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    # decoding tokens created
    @staticmethod
    def decode_auth_token(auth_token):
        """Decode the auth token"""
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Your signature has expired, Please login again.'
        except jwt.InvalidTokenError:
            return 'Your token is not valid. Please log in again.'
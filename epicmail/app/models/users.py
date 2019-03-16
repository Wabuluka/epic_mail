# empicmail/app/models.py
import datetime
import jwt
import re

from flask import jsonify, abort
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

    @staticmethod
    def validate_firstname(firstname):
        """Validation for the field of first name in the User model"""
        if not firstname:
            error = {
                "status": 401,
                "message":"You must provide the first name field"
            }
            return jsonify(error), 401
        elif len(str(firstname)) < 5:
            error = {
                "status": 401,
                "message":"Names accepted must be at least 5 characters"
            }
            return jsonify(error), 401
        elif not isinstance(firstname, str):
            error = {
                "status": 401,
                "message":"The name must be a string"
            }
            return jsonify(error), 401
        elif re.search("[0-9]", str(firstname)) or re.search("[$#@*&%!~`+=|':;.><,_-]", str(firstname)):
            error = {
                "status": 401,
                "message":"Do not use special characters and numbers on a name"
            }
            return jsonify(error), 401

    
    @staticmethod
    def validate_lastname(lastname):
        """Validation for the field of last name in the User model"""
        if not lastname:
            error = {
                "status": 401,
                "message":"You must provide the last name field"
            }
            return jsonify(error), 401
        elif len(str(lastname)) < 5:
            error = {
                "status": 401,
                "message":"Names accepted must be at least 5 characters"
            }
            return jsonify(error), 401
        elif not isinstance(lastname, str):
            error = {
                "status": 401,
                "message":"The name must be a string"
            }
            return jsonify(error), 401
        elif re.search("[0-9]", str(lastname)) or re.search("[$#@*&%!~`+=|':;.><,_-]", str(lastname)):
            error = {
                "status": 401,
                "message":"Do not use special characters and numbers on a name"
            }
            return jsonify(error), 401

    @staticmethod
    def validate_password(password_hash):
        if len(password_hash) < 4:
            error = {
                "status": 401,
                "message":"Your password must have 5 characters and above"
            }
            return jsonify(error)
        elif re.search('[0-9]',password_hash) is None:
            error = {
                "status": 401,
                "message":"Your password must at least a number in it"
            }
            return jsonify(error)
        elif re.search('[A-Z]',password_hash) is None:
            error = {
                "status": 401,
                "message":"Your password must at least contain an uppercase character"
            }
            return jsonify(error)
        elif re.search("[$#@*&%!~`+=|':;.><,_-]",password_hash) is None:
            error = {
                "status": 401,
                "message":"Your password must at least a special character"
            }
            return jsonify(error)

    @staticmethod
    def validate_email(email):
        email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if email  == None:
            error = {
                'status':401,
                'message': 'Make sure your email is well written'
            }
            return jsonify(error)

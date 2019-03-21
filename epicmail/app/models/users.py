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
    def __init__(self, user_id, email, firstname, lastname, password):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        # self.auth_token=auth_token
        self.registered_on = datetime.datetime.now()

    def to_dictionary(self):
        return {
            "id":self.user_id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "password":self.password,
            "registered_on":self.registered_on,
            # "token":self.auth_token
        }

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
    def validate_password(password):
        if len(password) < 4:
            error = {
                "status": 401,
                "message":"Your password must have 5 characters and above"
            }
            return jsonify(error)
        elif re.search('[0-9]',password) is None:
            error = {
                "status": 401,
                "message":"Your password must at least a number in it"
            }
            return jsonify(error)
        elif re.search('[A-Z]',password) is None:
            error = {
                "status": 401,
                "message":"Your password must at least contain an uppercase character"
            }
            return jsonify(error)
        elif re.search("[$#@*&%!~`+=|':;.><,_-]",password) is None:
            error = {
                "status": 401,
                "message":"Your password must at least a special character"
            }
            return jsonify(error)

    @staticmethod
    def validate_email(email):
        # re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        email = re.match(r"[^@]+@[^@]+\.[^@]+", email)
        if email  == None:
            error = {
                'status':401,
                'message': 'Make sure your email is well written'
            }
            return jsonify(error)
        elif email == '':
            error = {
                'status':401,
                'message': 'You must fill in the email field'
            }
            return jsonify(error)

import datetime
import jwt
import re

from flask import jsonify, abort
from epicmail.app import app, bcrypt


"""
All the models of the API and the relevant valis=dations are defined
"""

class User:
    """User Model contains the properties stored for a user"""

    users_list = []

    def __init__(self, email, firstname, lastname, password):
        self.id = len(User.users_list)+1
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()

    def to_dictionary(self):
        return {
            "id": self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "password":self.password,
            "registered_on":self.registered_on
        }
    @staticmethod
    def find_user_by_email(email):
        for user in User.users_list:
            if email == user.email:
                return user

    def create_user(self,email, firstname, lastname, password):
        if User.find_user_by_email(self.email):
            return {
                "status": 409,
                "message": "Email already exists."
            }
        else:
            user = User(email, firstname,lastname, password)
            User.users_list.append(user)
            return {
                "status": 201,
                "message": "You have successfully created an account.",
                "data": user.to_dictionary()
            }

    @staticmethod
    def login_user(email, password):
        user = User.find_user_by_email(email)
        if user:
            if password == user.password:
                return {
                    "status": 201,
                    "message": "You have successfully logged in."
                }
        return {
            "status": 401,
            "message": "Wrong credentials."
        }
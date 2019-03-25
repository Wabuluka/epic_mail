import datetime
import jwt
import re

from flask import jsonify, abort
from app import app, bcrypt
from app.models.db import DatabaseConnection

database=DatabaseConnection()
cur=database.cursor

database.create_user_table()


"""
All the models of the API and the relevant valis=dations are defined
"""

class User:
    """User Model contains the properties stored for a user"""

    users_list = []

    def __init__(self, **kwargs):
        self.firstname=kwargs.get('firstname')
        self.lastname=kwargs.get('lastname')
        self.email=kwargs.get('email')
        self.password=kwargs.get('password')
        self.registered_on=datetime.datetime.utcnow()

    def to_dictionary(self):
        return {
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

    def create_user(self, user):
        """Create a new user"""
        query = """
            INSERT INTO users(firstname, lastname, email, password, registered_on)
            VALUES('{}', '{}', '{}', '{}', '{}')""".format(user.firstname, user.lastname,
            user.email, user.password, user.registered_on)
        cur.execute(query)

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
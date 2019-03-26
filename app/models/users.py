import datetime
import jwt
import re

from flask import jsonify, abort
from app import app, bcrypt
from app.models.db import DatabaseConnection

database=DatabaseConnection()
cur=database.cursor
database.drop_tables()
database.create_user_table()


"""
All the models of the API and the relevant valis=dations are defined
"""

class User:
    """User Model contains the properties stored for a user"""

    # users_list = []

    def __init__(self, **kwargs):
        self.firstname=kwargs["firstname"]
        self.lastname=kwargs['lastname']
        self.email=kwargs['email']
        self.password=kwargs['password']
        self.registered_on=datetime.datetime.utcnow()

#     @classmethod
#     def to_dictionary(cls):
#         return {
#             "firstname":cls.firstname,
#             "lastname":cls.lastname,
#             "email":cls.email,
#             "password":cls.password,
#             "registered_on":cls.registered_on
# }

    @staticmethod
    def get_user_by_email(email):
        query = """
            SELECT * FROM users WHERE email = '{}'
        """.format(email)
        cur.execute(query)
        return cur.fetchone()
    

    # def __str__(self):
    #     return "'{}'".format(self.email)


    def create_user(self):
        """Create a new user"""
        query = "INSERT INTO users(firstname, lastname, email, password, registered_on)\
            VALUES('{}', '{}', '{}', '{}', '{}') RETURNING *;".format(
                self.firstname, 
                self.lastname,
                self.email,
                self.password, 
                # bcrypt.generate_password_hash(self.password, app.config.get('BCRYPT_LOG_ROUNDS')).decode(), 
                self.registered_on)
        cur.execute(query)
        return cur.fetchone()
 
        
    @staticmethod
    def login_user(email, password):
        query = "SELECT email, password FROM users WHERE email='{}' AND password='{}'".format(email, password)
        cur.execute(query)
        return cur.fetchone()
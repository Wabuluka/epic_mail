import datetime

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

    def __init__(self, **kwargs):
        self.firstname=kwargs["firstname"]
        self.lastname=kwargs['lastname']
        self.email=kwargs['email']
        self.password=kwargs['password']
        self.registered_on=datetime.datetime.utcnow()

    @staticmethod
    def get_user_by_email(email):
        query = """
            SELECT * FROM users WHERE email = '{}'
        """.format(email)
        cur.execute(query)
        return cur.fetchone()
    
    @staticmethod
    def get_user_id(email):
        query = """
            SELECT user_id FROM users WHERE email = '{}'
        """.format(email)
        cur.execute(query)
        return cur.fetchone()

    def create_user(self):
        """Create a new user"""
        query = "INSERT INTO users(firstname, lastname, email, password, registered_on)\
            VALUES('{}', '{}', '{}', '{}', '{}') RETURNING *;".format(
                self.firstname, 
                self.lastname,
                self.email,
                self.password, 
                self.registered_on)
        cur.execute(query)
        return cur.fetchone()
     
    @staticmethod
    def login_user(email, password):
        query = "SELECT email, password FROM users WHERE email='{}' AND password='{}'".format(email, password)
        cur.execute(query)
        return cur.fetchone()
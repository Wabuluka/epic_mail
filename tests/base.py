from flask_testing import TestCase
import unittest
import json
from app import app, jwt
from app.models.db import DatabaseConnection
from app.config import TestingConfig
from flask_jwt_extended import create_access_token, decode_token

SECRET_KEY="dfsgshshghdghsghsdghsdhgsd"
database=DatabaseConnection()
class BaseTestCase(unittest.TestCase):
    """Base Tests"""

    def setUp(self):
        self.app = app.test_client()
        database = DatabaseConnection()
        database.create_user_table()
        database.create_user_table()
        database.create_messages_table()

        # create user for testing sign up
        self.create_user={
            "firstname":"test",
            "lastname":"test",
            "email":"test@gmail.com",
            "password":"Test@123"
        }

        # login user for testing
        self.login_user={
            "user_id":1,
            "email":"test@gmail.com",
	        "password":"Test@123"
        }

        # test create a message
        self.create_message={
            "subject":"Hello world",
            "message":"I had taken long with out seeing you so i decided to message you to see if we can schedule a meet up",
            "address":"webbiewabuluka@gmail.com",
            "createdby":1,
            "status":"sent"
        }

        # creating a token
        self.token = create_access_token(
            {"user_id": self.login_user['user_id']
            },
            SECRET_KEY).decode('UTF-8')
        # getting the token to the header
        self.headers = {
            "Authorization": f"Bearer {self.token}"
            }


    def tearDown(self):
        database.drop_tables()
        
from flask_testing import TestCase
from app import app
from app.models.db import DatabaseConnection
import json
from flask_jwt_extended import create_access_token


class BaseTestCase(TestCase):
    """ Base Tests """
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def setUp(self):
        self.app=app.test_client()
        database=DatabaseConnection()
        database.create_user_table()
        database.create_messages_table()
        database.create_groups_table()
        database.create_group_members_table()
        database.create_group_mail()  

        self.user_one={
            "email": "test@gmail.com",
            "firstname": "test",
            "lastname": "test",
            "password": "Test@123",
            "registered_on": "Tue, 26 Mar 2019 13:36:58 GMT",
            "user_id": 1
        }
        self.user_one={
            "email": "test1@gmail.com",
            "firstname": "test1",
            "lastname": "test1",
            "password": "Test1@123",
            "registered_on": "Tue, 26 Mar 2019 13:36:58 GMT",
            "user_id": 1
        }
        self.user_login={
            "email":"test1@gmail.com",
	        "password":"Test1@123"
        }
        self.message={
            "subject":"Hello world",
            "message":"I had taken long with out seeing you so i decided to message you to see if we can schedule a meet up",
            "address":2,
            "status":"sent"
        }
        self.group_one={
            "group_name":"webblots_1",
            "role":"we are here to be who we are",
            "createdby":1
        }
        self.group_two={
            "group_name":"webblots_1",
            "role":"we are here to be who we are",
            "createdby":1
        }
        self.group_member={
            "group_id":1,
	        "member":1
        }
        self.group_msg={
            "subject": "heading of the message",
            "message":"Lorem ipsum of the message that am going to write to you for this moment",
            "status":"send"
        }
    def create_token(self):
        id={'user_id':1}
        token=create_access_token(identity=id)
        print(token)
        return token

    def tearDown(self):
        database=DatabaseConnection()
        database.drop_tables()
# epicmail/tests/test_user.py
import time
import json
import datetime
import unittest

from epicmail.app.models.users import User, users
from epicmail.tests.base import BaseTestCase
from epicmail.app.handler.auth import JwtAuth

authentic = JwtAuth()

def signup_new_user(self, email, firstname, lastname, password):
    """Mock data for testing user signup"""
    return self.client.post(
        '/epicmail/api/v2/auth/signup',
        data=json.dumps(dict(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password
        )),
        content_type='application/json',
    )

def user_login(self, email, password):
    return self.client.post(
        '/epicmail/api/v2/auth/login',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )


class TestSignUp(BaseTestCase):
    """Test if the user gets created"""
    def test_user_registration(self):
        """Test user account creation"""
        with self.client:
            response = self.client.post(
                '/epicmail/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 201)
            self.assertTrue(data['message'] == "You have successfully created an account.")

    # def test_user_already_exists(self):
    #     """Test if a user with given email already in the system"""
    #     # def test_user_registration_with_same_account(self):
    #         # """Test user account creation"""
    #     with self.client:
    #         response = self.client.post(
    #             '/epicmail/api/v2/auth/signup',
    #             data=json.dumps(dict(
    #                 firstname='Davies',
    #                 lastname='Wabuluka',
    #                 email = 'dwabuluka@gmail.com',
    #                 password= 'Watis@123'
    #             )),
    #             content_type='application/json'
    #         )
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['message'] == "User with that email already exists, please try with another email.")


    # def test_login(self):
    #     """Test if a user can login"""
    #     resp_login = self.client.post(
    #         '/epicmail/api/v2/auth/login',
    #         data=json.dumps(dict(
    #             email='dw1abuluka@gmail.com',
    #             password='Watis1@123'
    #         )),
    #         content_type='application/json',
    #     )
    #     login_data = json.loads(resp_login.data.decode())
    #     # self.assertTrue(login_data['status'] == 200)
    #     self.assertTrue(data_register['auth_token'])

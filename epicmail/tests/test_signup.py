# epicmail/tests/test_user.py
import time
import json
import datetime
import unittest

from epicmail.app.models.users import User, users
from epicmail.tests.base import BaseTestCase

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





# class TestUserAuth(BaseTestCase):

#     def test_registration(self):
#         with self.client:
#             response = signup_new_user(self, 'wabuluka', 'davies','dwabuluka@gmail.com', 'gdchjdjfhj@ndn')
#             data = json.loads(response.data.decode())
#             self.assertTrue(data['status'] == 201)
#             self.assertTrue(data['message'] == 'You have successfully created an account')
#             self.assertTrue(response.content_type == 'application/json')
#             self.assertEqual(response.status_code, 201)

#     def test_user_already_exists(self):
#         """A user must register only once"""
#         user = User(
#             user_id=len(users)+1,
#             firstname='wabuluka',
#             lastname='daviesd',
#             email='dwabuluka@gmail.com',
#             password='whatdoyouwant@123'
#         )
#         users.append(user)
#         with self.client:
#             response = signup_new_user(self, 'wabuluka', 'daviesd','dwabuluka@gmail.com', 'gdchjdjfhj@ndn')
#             data = json.loads(response.data.decode())
#             self.assertTrue(data['status'] == 202)
#             self.assertTrue(
#                 data['message'] == 'User with that email already exists, please try with another email')
#             self.assertEqual(response.status_code, 202)

            
        
    # def test_user_login(self):
    #     with self.client:
    #         u_login = signup_new_user(self, 'wabuluka', 'davies','dwabuluka@gmail.com', 'gdchjdjfhj@ndn')
    #         d_login = json.loads(u_login.data.decode())
    #         self.assertTrue(d_login['status':'Successfully logged in.'])
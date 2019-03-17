# epicmail/tests/test_user.py

import unittest

from epicmail.app.models.users import User, users
from epicmail.tests.base import BaseTestCase

class TestUserModel(BaseTestCase):
    def test_encode_authentication_token(self):
        """Test if the Token gets encoded(created)"""
        user = User(
            user_id=len(users)+1,
            firstname='Daviesd',
            lastname='Wabuluka',
            email='dwabuluka@gmail.com',
            password='whatdoyouwant@123'
        )
        users.append(user)
        auth_token = user.encode_auth_token(user.user_id)
        self.assertTrue(isinstance(auth_token, bytes))

    # def test_decode_authentication_token(self):
    #     """Test if the Token gets decoded(understood)"""
    #     user = User(
    #         user_id=len(users)+1,
    #         firstname='Daviesd',
    #         lastname='Wabuluka',
    #         email='dwabuluka@gmail.com',
    #         password='whatdoyouwant@123'
    #     )
    #     users.append(user)
    #     auth_token = user.decode_auth_token(user.user_id)
        # self.assertTrue(isinstance(auth_token, bytes))
        # self.assertTrue(user.decode_auth_token(auth_token) == 1)will be rectified in the future

    

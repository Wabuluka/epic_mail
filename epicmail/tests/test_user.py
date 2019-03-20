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

    def test_decode_auth_token(self):
        user = User(
            user_id = len(users)+1,
            firstname='Davies',
            lastname='Wabuluka',
            email = 'dwabuluka@gmail.com',
            password= 'Watis@123'
        )
        users.append(user)
        auth_token = user.encode_auth_token(user.user_id)
        self.assertTrue(isinstance(auth_token, bytes))
        # self.assertTrue(User.decode_auth_token(auth_token)==1)
        self.assertTrue(User.decode_auth_token(auth_token))


if __name__=='__main__':
    unittest.main()
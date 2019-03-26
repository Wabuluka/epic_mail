import time
import json
import datetime
import unittest

from app.models.users import User
from tests.base import BaseTestCase



def signup_new_user(self, email, firstname, lastname, password):
    """Mock data for testing user signup"""
    return self.client.post(
        '/api/v3/auth/signup',
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
        '/api/v3/auth/login',
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
                '/api/v3/auth/signup',
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
            self.assertTrue(data['message'] == "You have successfully created an account")

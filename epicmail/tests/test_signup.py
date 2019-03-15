# epicmail/tests/test_user.py
import time
import json
import datetime
import unittest

from epicmail.app.models import User, users
from epicmail.tests.base import BaseTestCase

def signup_new_user(self, email, firstname, lastname, password_hash):
    return self.client.post(
        'auth/signup',
        data=json.dumps(dict(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password_hash=password_hash
        )),
        content_type='application/json',
    )


class TestUserAuth(BaseTestCase):

    def test_registration(self):
        with self.client:
            response = signup_new_user(self, 'wabuluka', 'davies','dwabuluka@gmail.com', 'gdchjdjfhj@ndn')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == '201')
            self.assertTrue(data['message'] == 'You have successfully created an account')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


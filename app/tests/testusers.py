import unittest
import datetime
import json
from flask import jsonify
from app.tests.testbase import BaseTestCase
from app.tests import create_user


class TestUser(BaseTestCase):
    '''Holds all tests about the users in the app'''

    def test_signup(self):
        data = create_user()

        response = self.client().post('/signup', content_type = 'application/json', data=json.dumps(data))
        self.assertEqual(response.status_code, 201)
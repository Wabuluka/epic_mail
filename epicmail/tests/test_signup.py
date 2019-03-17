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

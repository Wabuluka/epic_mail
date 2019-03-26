import unittest
import json
from flask import jsonify
from tests.base import BaseTestCase


class TestUser(BaseTestCase):

    def create_user_login(self):
        new_user=self.app.post(
            "/api/v2/auth/signup",
            content_type='application/json',
            data=json.dumps(self.create_user)
            )
        return new_user

    def login_user_created(self):
        logged_in_user = self.app.post(
            "/api/v2/auth/login",
            content_type='application/json',
            data=json.dumps(self.login_user)
            )
        return logged_in_user

    # def test_user_signup(self):
    #     signup = self.create_user_login()
    #     self.assertEquals(signup.status_code, 201)


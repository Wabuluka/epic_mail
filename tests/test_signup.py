import  unittest
import json
from app.models.db import DatabaseConnection
from app.models.users import User
from tests.base import BaseTestCase
from flask_jwt_extended import create_access_token

database=DatabaseConnection()


class TestUserModel(BaseTestCase):

    def test_login(self):
        self.create_token()
        with self.app as d:
            response=d.post('/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user_login))
            self.assertEqual(response.status_code, 200)
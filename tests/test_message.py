import  unittest
import json
from app.models.db import DatabaseConnection
from app.models.users import User
from tests.base import BaseTestCase
from flask_jwt_extended import create_access_token

database=DatabaseConnection()


class TestUserModel(BaseTestCase):

    def test_message_create(self):
        token=self.create_token() 
        with self.app as d:
            d.post('/api/v2/auth/signup',
                content_type='application/json',
                data=json.dumps(self.user_one))
            response=d.post('/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user_login))
            self.assertEqual(response.status_code, 200)
            d.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)

    def test_get_one_messages(self):
        token=self.create_token()
        with self.app as d:
            d.post('/api/v2/auth/signup',
                content_type='application/json',
                data=json.dumps(self.user_one))
            response=d.post('/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user_login))
            self.assertEqual(response.status_code, 200)
            d.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)
            d.get('/api/v2/messages/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)

    def test_delete_one(self):
        token=self.create_token()
        with self.app as d:
            d.post('/api/v2/auth/signup',
                content_type='application/json',
                data=json.dumps(self.user_one))
            response=d.post('/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user_login))
            self.assertEqual(response.status_code, 200)
            d.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)
            d.get('/api/v2/messages/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)
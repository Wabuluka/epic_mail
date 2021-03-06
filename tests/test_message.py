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
        with self.app:
            response = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(dict(
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            self.app.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.assertEqual(response.status_code,200)

    def test_get_one_messages(self):
        token=self.create_token() 
        with self.app:
            response = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(dict(
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            self.app.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.app.get('/api/v2/messages/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json')
            self.assertEqual(response.status_code,200)

    def test_delete_one(self):
        token=self.create_token() 
        with self.app:
            response = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(dict(
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            self.app.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.app.delete('/api/v2/messages/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json')
            self.assertEqual(response.status_code,200)

    def test_get_all_messages(self):
        token=self.create_token() 
        with self.app:
            response = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(dict(
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            self.app.post('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.message))
            self.app.get('/api/v2/messages',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json')
            self.assertEqual(response.status_code,200)
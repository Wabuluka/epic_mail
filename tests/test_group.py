import  unittest
import json
from app.models.db import DatabaseConnection
from app.models.group_model import Group
from tests.base import BaseTestCase
from flask_jwt_extended import create_access_token

database=DatabaseConnection()


class TestUserModel(BaseTestCase):
    
    def test_create_group(self):
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
            self.app.post('/api/v2/groups',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.group_one))
            self.assertEqual(response.status_code,200)
    
    def test_delete_group(self):
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
            self.app.post('/api/v2/groups',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.group_two))
            self.app.delete('/api/v2/groups/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json')
            self.assertEqual(response.status_code,200)
    
    # def test_add_member(self):
    #     token=self.create_token() 
    #     with self.app:
    #         response = self.client.post(
    #             '/api/v2/auth/signup',
    #             data=json.dumps(dict(
    #                 firstname='Davies',
    #                 lastname='Wabuluka',
    #                 email = 'dwabuluka@gmail.com',
    #                 password= 'Watis@123'
    #             )),
    #             content_type='application/json'
    #         )
    #         response = self.client.post(
    #             '/api/v2/auth/login',
    #             data=json.dumps(dict(
    #                 email = 'dwabuluka@gmail.com',
    #                 password= 'Watis@123'
    #             )),
    #             content_type='application/json'
    #         )
    #         self.app.post('/api/v2/groups',headers=dict(Authorization= 'Bearer '+token),
    #             content_type='application/json',
    #             data=json.dumps(self.group_one))
    #         self.assertEqual(response.status_code, 200)
    #         self.app.post('/api/v2/groups/1/users',headers=dict(Authorization= 'Bearer '+token),
    #             content_type='application/json',
    #             data=json.dumps(self.group_member))
    #         self.assertEqual(response.status_code,201)

    def test_delete_member(self):
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
            self.app.post('/api/v2/groups',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.group_one))
            self.assertEqual(response.status_code, 200)
            self.app.post('/api/v2/groups/1/users',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json',
                data=json.dumps(self.group_member))
            self.app.delete('/api/v2/groups/1/users/1',headers=dict(Authorization= 'Bearer '+token),
                content_type='application/json')
            self.assertEqual(response.status_code,200)

    # def test_create_message(self):
    #     token=self.create_token() 
    #     with self.app:
    #         response = self.client.post(
    #             '/api/v2/auth/signup',
    #             data=json.dumps(dict(
    #                 firstname='Davies',
    #                 lastname='Wabuluka',
    #                 email = 'dwabuluka@gmail.com',
    #                 password= 'Watis@123'
    #             )),
    #             content_type='application/json'
    #         )
    #         response = self.client.post(
    #             '/api/v2/auth/login',
    #             data=json.dumps(dict(
    #                 email = 'dwabuluka@gmail.com',
    #                 password= 'Watis@123'
    #             )),
    #             content_type='application/json'
    #         )
    #         self.app.post('/api/v2/groups',headers=dict(Authorization= 'Bearer '+token),
    #             content_type='application/json',
    #             data=json.dumps(self.group_one))
    #         self.assertEqual(response.status_code, 200)
    #         self.app.post('/api/v2/groups/1/messages',headers=dict(Authorization= 'Bearer '+token),
    #             content_type='application/json',
    #             data=json.dumps(self.group_msg))
    #         self.assertEqual(response.status_code, 200)
            
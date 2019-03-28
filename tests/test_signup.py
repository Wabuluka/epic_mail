import  unittest
import json
from app.models.db import DatabaseConnection
from app.models.users import User
from tests.base import BaseTestCase
from flask_jwt_extended import create_access_token

database=DatabaseConnection()


class TestUserModel(BaseTestCase):

    def signup_new_user(self, email, firstname, lastname, password):
        """Mock data for testing user signup"""
        return self.client.post(
            '/api/v2/auth/signup',
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
        '/api/v2/auth/login',
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
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = 'dwabuluka@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,201)
            self.assertTrue(data['status'] == 201)
            self.assertTrue(data['message'] == "You have successfully created an account")


    def signup_with_wrong_email(self):
        with self.client:
            response = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(dict(
                    firstname='Davies',
                    lastname='Wabuluka',
                    email = '@gmail.com',
                    password= 'Watis@123'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            # self.assertEqual(response.status_code,201)
            self.assertTrue(data['status'] == 400)
            self.assertTrue(data['message'] == "please input valid email")

    def test_login(self):
        with self.client:
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
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,200)
            self.assertTrue(data['status'] == 200)
            self.assertTrue(data['message'] == "You are logged in successfully")
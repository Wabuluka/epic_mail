# epicmail/tests/test_message.py

import unittest
import json

from epicmail.app.models.users import User, users
from epicmail.tests.base import BaseTestCase


def send_message(self, subject, message, address, createdby, status):
        return self.client.post(
        '/epicmail/api/v2/messages',
        data=json.dumps(dict(
            subject=subject,
            message=message,
            address=address,
            createdby=createdby,
            status=status
        )),
        content_type='application/json',
    )


class TestMessageModel(BaseTestCase):
    """All tests for the Messages"""

    def test_message_created(self):
        with self.client:
            response = send_message(self, 'Hello world', 'I had taken long w',
                                    'wwwwwwwww@gmail.com', 'dwabuluka@gmail.com', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 201)
            self.assertTrue(data['message'] == 'Your message has been successfully sent.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_subject_field_is_provided(self):
        with self.client:
            response = send_message(self, '', 'I had taken long w',
                                    'wwwwwwwww@gmail.com', 'dwabuluka@gmail.com', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 401)
            self.assertTrue(data['error'] == 'You must fill the subject field.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_message_field_is_provided(self):
        with self.client:
            response = send_message(self, 'Hello world', '',
                                    'wwwwwwwww@gmail.com', 'dwabuluka@gmail.com', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 401)
            self.assertTrue(data['error'] == 'You must fill the message field.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_address_field_is_provided(self):
        with self.client:
            response = send_message(self, 'Hello world', 'to day was a fairy tale',
                                    '', 'dwabuluka@gmail.com', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 401)
            self.assertTrue(data['error'] == 'You must fill the address field.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    # def test_address_field_is_correct(self):
    #     with self.client:
    #         response = send_message(self, 'Hello world', 'to day was a fairy tale',
    #                                 '', 'dwabuluka@gmail.com', 'sent')
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 401)
    #         self.assertTrue(data['error'] == 'Make sure your address is well written.')
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 401)

    def test_created_field_is_provided(self):
        with self.client:
            response = send_message(self, 'Hello world', 'to day was a fairy tale',
                                    'dwasn@gmail.com', '', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 401)
            self.assertTrue(data['error'] == 'You must fill the createdby field.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_getting_all_messages_created(self):
        with self.client:
            response = send_message(self, 'Hello world', 'I had taken long w',
                                    'wwwwwwwww@gmail.com', 'dwabuluka@gmail.com', 'sent')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 201)
            data = json.dumps(response.data.decode())
            self.assertTrue(data['status'] == 200)
# epicmail/tests/test_message.py

import unittest
import json

from epicmail.app.models.users import User, users
from epicmail.tests.base import BaseTestCase


def send_message(self, subject, message, address, createdby, status):
        return self.client.post(
        '/messages',
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
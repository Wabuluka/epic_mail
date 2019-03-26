import unittest
import json

from app.models.users import User
from tests.base import BaseTestCase


def send_message(self, subject, message, address, createdby, status):
        return self.client.post(
        '/api/v3/messages',
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
    pass
    # def test_message_created(self):
    #     with self.client:
            
    #         response = send_message(self, 'Hello world', 'I had taken long w',
    #                                 'wwwwwwwww@gmail.com', 'dwabuluka@gmail.com', 'sent')
    #         data = json.loads(response.data.decode())
    #         self.assertTrue(data['status'] == 201)
    #         self.assertTrue(data['message'] == 'Message has been created successfully')
    #         self.assertTrue(response.content_type == 'application/json')
    #         self.assertEqual(response.status_code, 201)

    
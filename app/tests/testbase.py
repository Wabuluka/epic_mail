import unittest
import os
import json
from app import create_app
from app.users.model import User

class BaseTestCase(unittest.TestCase):
    '''Setup the testing base, all tests will run from this base'''

    def setUp(self):
        '''Initializing the app'''
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
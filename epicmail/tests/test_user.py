# epicmail/tests/test_user.py

import unittest

from epicmail.app.models.users import User
from epicmail.tests.base import BaseTestCase
from epicmail.app.handler.auth import JwtAuth

authentic = JwtAuth()



if __name__=='__main__':
    unittest.main()
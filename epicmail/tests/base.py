from flask_testing import TestCase

from epicmail.app import app


class BaseTestCase(TestCase):
    """Base Tests"""

    def create_app(self):
        app.config.from_object('epicmail.app.config.TestingConfig')
        return app
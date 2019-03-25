import unittest

from flask import current_app
from epicmail.app import app
from flask_testing import TestCase

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('epicmail.app.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['DATABASE_URI'] == 'postgresql://postgres:root123@localhost/challengethree'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('epicmail.app.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['DATABASE_URI'] == 'postgresql://postgres:root123@localhost/challengethree_test'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('epicmail.app.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()

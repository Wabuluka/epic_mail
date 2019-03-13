# instance/config.py
import os
base_directory = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''Main configuration class.'''
    DEBUG = False
    SECRET = os.getenv('SECRET')


class DevolopmentConfiguration(Config):
    '''Development configurations'''
    DEBUG = True


class TestingConfiguration(Config):
    '''Testing configuration'''
    TESTING = True
    DEBUG = True


class StagingConfiguration(Config):
    '''Staging configuration'''
    DEBUG = True


class ProductionConfiguration(Config):
    '''Production configuration'''
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevolopmentConfiguration,
    'testing': TestingConfiguration,
    'staging': StagingConfiguration,
    'production': ProductionConfiguration,
}
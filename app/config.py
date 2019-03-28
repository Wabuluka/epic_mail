import os

postgres_local_base = 'postgresql://postgres:root123@localhost/'
database_name = "challengethree"
class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'its me your boy the bad guy')
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = postgres_local_base + database_name



class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DATABASE_URI = postgres_local_base + database_name +"_test"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'its me your boy the bad guy'
    DEBUG = False
    DATABASE_URI = 'postgresql:///'

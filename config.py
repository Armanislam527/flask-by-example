import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = 'postgresql://arman:Iamarman1khan@localhost/arman'
    #REDIS_URL = "redis://localhost:6379/0"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://flask:password@db/flask_app')
    # REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://arman:Iamarman1khan@localhost/arman')
    REDIS_URL = os.environ.get('REDIS_URL', "redis://localhost:6379/0")

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

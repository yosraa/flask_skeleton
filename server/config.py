# server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(
        os.path.join(basedir, 'test_dev.db'))


class TestingConfig(BaseConfig):
    """Testing configuration."""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    #BCRYPT_LOG_ROUNDS = 13
    # POSTGRES = {
    #     'user': 'postgres',
    #     'pw':'root',
    #     'db': 'LAFAYETTE',
    #     'host': 'localhost',
    #     'port': '5432',
    # }
    # SQLALCHEMY_DATABASE_URI= 'postgresql://%(user)s:\
    # %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    pass
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/examplee'
    #WTF_CSRF_ENABLED = True

import secrets
import datetime


class Config(object):
    PORT = 3000
    DEBUG = True
    TESTING = False
    HOST = "127.0.0.1"
    SESSION_TYPE = 'filesystem'
    SESSION_USE_SIGNER = True
    SECRET_KEY = secrets.token_hex(16)
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=24)
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    PORT = 80
    DEBUG = False
    HOST = "0.0.0.0"
    SQLALCHEMY_DATABASE_URI = 'postgresql://cowanweks:ultimate@localhost/timetabler'

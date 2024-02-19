import secrets


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = '3f93169b2c2f35c1d1ff06cc0d0a3232'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://cowanweks:ultimate@localhost/timetabler'


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True

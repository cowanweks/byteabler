
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://cowanweks:ultimate@localhost/timetabler'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

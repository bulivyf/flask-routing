import os

basedir = os.path.abspath(os.path.dirname(__file__))

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))


class Config:
    SECRET_KEY = b'\x83\xfble\xea\x15\xebT9Hu\t\xcdx\x16^\xf1=\xceo\x05i\x8d\xd1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ref.db')


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../tests/test.db')
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"
    # print("TestingConfig: DB location: " + SQLALCHEMY_DATABASE_URI)


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ref.db')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

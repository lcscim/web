#__author__:asus
#date:2018/10/28
#通过调用该文件的不同的类来实现不同的方法
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'asdsadsadas'


class TestingConfig(Config):
    TESTING = True
#__author__:asus
#date:2018/11/6
from redis import Redis


class BaseConfig(object):
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='192.168.0.94', port='6379')
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@127.0.0.1:3306/s9day120?charset=utf8"
    SQLALCHEMY_POOL_SIZE=10
    SQLALCHEMY_MAX_OVERFLOW=5

class ProConfig(BaseConfig):
    pass
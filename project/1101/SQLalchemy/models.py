#__author__:asus
#date:2018/11/2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    # email = Column(String(32), unique=True)
    # ctime = Column(DateTime, default=datetime.datetime.now)
    # extra = Column(Text, nullable=True)


def create_all():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:@127.0.0.1:3306/s9day118?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)

def drop_all():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:@127.0.0.1:3306/s9day118?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    create_all()
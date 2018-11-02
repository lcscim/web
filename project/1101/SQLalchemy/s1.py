#__author__:asus
#date:2018/11/2
from models import Users
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine=create_engine(
    "mysql+pymysql://root:@127.0.0.1:3306/s9day118?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）

)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

#增加
# obj = Users(name='alex')
# session.add(obj)
# session.add_all([
#     Users(name='小东北'),
#     Users(name='龙泰')
# ])
# session.commit()
#查找
# result=session.query(Users).all()
# result=session.query(Users).filter(Users.id>=2)
# for row in result:
#     print(row.id,row.name)
#删
# session.query(Users).filter(Users.id>=2).delete()
# session.commit()
#改
session.query(Users).filter(Users.id==1).update({Users.name:'lex'})
session.commit()


session.close()
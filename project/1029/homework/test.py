#__author__:asus
#date:2018/10/30

#加密
# import hashlib
#
# hash=hashlib.md5(b"sdf1123df")
# hash.update(bytes('123',encoding='utf-8'))
# ret=hash.hexdigest()
# print(ret)


#数据库操作
# import pymysql
#
# conn=pymysql.connect(host='127.0.0.1',user='root',password='',charset='utf8',database='s9day118')
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor.execute('select * from userinfo where user=%s and pwd=%s',("xiaoqiang","47f5abdd7f4083f0cc5c94d587fa3ca4"))
# #date = cursor.fetchall()
# date = cursor.fetchone()
# cursor.close()
# conn.close()
# print(date)

#解压文件
import shutil

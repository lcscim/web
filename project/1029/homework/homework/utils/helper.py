#__author__:asus
#date:2018/10/31
from settings import Config
import pymysql

def featch_all(sql,args):
    conn = Config.POOL.connect()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    record_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return record_list

def featch_one(sql,args):
    conn = Config.POOL.connect()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert(sql,args):
    conn = Config.POOL.connect()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    row = cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()
    return row
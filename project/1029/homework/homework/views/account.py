#__author__:asus
#date:2018/10/30
from flask import Blueprint ,render_template,request,redirect,session
import pymysql
from ..utils.md5 import md5
from ..utils import helper

account=Blueprint('account',__name__)

@account.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    username=request.form.get('user')
    password=request.form.get('pwd')
    pwd_md5=md5(password)
    # conn = Config.POOL.connect()
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute('select id,nickname from userinfo where user=%s and pwd=%s', (username,pwd_md5))
    # date = cursor.fetchone()
    # cursor.close()
    # conn.close()
    date=helper.featch_one('select id,nickname from userinfo where user=%s and pwd=%s', (username,pwd_md5))

    if not date:
        return render_template('login.html',error="用户名或密码错误")
    session['user_info']={'id':date['id'],'nickname':date['nickname']}
    return redirect('/index')


@account.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']
    return redirect('/login')


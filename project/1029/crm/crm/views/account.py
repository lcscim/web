#__author__:asus
#date:2018/10/29
from flask import Blueprint
#template_folder='',static_url_path=''指定模板路径和静态文件
ac=Blueprint('ac',__name__)

@ac.route('/login')
def login():
    return "login"\

@ac.route('/logout')
def logout():
    return "logout"
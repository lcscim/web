#__author__:asus
#date:2018/11/6

from flask import Blueprint

ac=Blueprint('ac',__name__)

@ac.route('/login')
def login():
    return 'login'
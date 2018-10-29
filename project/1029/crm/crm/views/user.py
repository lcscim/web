#__author__:asus
#date:2018/10/29
from flask import Blueprint

uc=Blueprint('uc',__name__)

@uc.route('/list')
def list():
    return "list"

@uc.route('/detail')
def detail():
    return "detail"
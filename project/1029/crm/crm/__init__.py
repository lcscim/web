#__author__:asus
#date:2018/10/29
from flask import Flask
from .views.account import ac
from .views.user import uc

def create_app():
    app = Flask(__name__)
    #表示访问ac路径下的路径需要在前面添加admin
    app.register_blueprint(ac,url_prefix='/admin')
    app.register_blueprint(uc)
    return app


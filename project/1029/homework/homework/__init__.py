#__author__:asus
#date:2018/10/29
from flask import Flask
from .views.account import account
from .views.index import ind

def create_app():
    app=Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(account)
    app.register_blueprint(ind)


    return app
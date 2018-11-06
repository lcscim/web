#__author__:asus
#date:2018/11/6
from flask import Flask
from .views.account import ac
from .views.user import us
from flask_session import Session
#第一步：导入sqlalchemy并实例化
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object('settings.ProConfig')

    app.register_blueprint(ac)
    app.register_blueprint(us)

    # Session(app)
    #导入app中的配置文件中关于sqlalchemy的信息
    db.init_app(app)

    return app
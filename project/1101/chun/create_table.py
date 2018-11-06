#__author__:asus
#date:2018/11/6
from chun import db,create_app

app=create_app()

app_ctx=app.app_context()

with app_ctx:
    db.create_all()
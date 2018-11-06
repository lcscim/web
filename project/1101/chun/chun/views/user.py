#__author__:asus
#date:2018/11/6

from flask import Blueprint
from chun import db
from chun import models

us=Blueprint('us',__name__)

@us.route('/index')
def index():
    db.session.add(models.Users(name='高件套',depart_id=1))
    db.session.commit()
    db.session.remove()

    return 'index'
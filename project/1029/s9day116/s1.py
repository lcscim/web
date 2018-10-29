#__author__:asus
#date:2018/10/29
from flask import Flask,views
app=Flask(__name__)
import functools

def wrapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@app.route('/index')
def index():
    return "index"


def log():
    return "log"
app.add_url_rule("/login",None,log)

class UsrView(views.MethodView):
    methods=['GET']
    decorators=[wrapper,]
    def get(self,*args,**kwargs):
        return "GET"
    def post(self,*args,**kwargs):
        return "POST"
app.add_url_rule('/user',None,UsrView.as_view('uuuu'))

if __name__ == '__main__':
    app.run()
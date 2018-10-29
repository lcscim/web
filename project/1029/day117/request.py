#__author__:asus
#date:2018/10/29
from flask import Flask

app=Flask(__name__)

@app.route('/index')
def index():
    return "hello"

if __name__=='__main__':
    app.run()
    app.__call__
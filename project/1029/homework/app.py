# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
from homework import create_app

app=create_app()

if __name__ == '__main__':
    app.run()

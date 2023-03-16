from time import time
from flask import Flask
import time

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<h1>{func()}</h1>"
    return wrapper

def underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/')
@make_bold
@underline
def welcome():
    return 'welcome'

@app.route('/user/<name>/<int:age>')
def user(name,age):
    return { 'name': name, 'age':age}



if __name__ == '__main__':
    app.run(debug=True)
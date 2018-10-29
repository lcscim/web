#__author__:asus
#date:2018/10/29
import functools

def wrapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


@wrapper
def index():
    pass
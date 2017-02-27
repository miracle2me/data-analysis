#coding=utf-8

import logging

def use_logging(func):
    def wrapper(*args, **kwargs):
        # 打印函数名 print func name
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def bar():
    print('i am bar')

@use_logging
def foo():
    print("I am foo")

bar()



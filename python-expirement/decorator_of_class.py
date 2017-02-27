#coding=utf-8

class Foo(object):
    def __init__(self,func):
        # 内部调用命名规范 _func
        self._func = func

    # 重写调用函数
    def __call__(self):
        print('class decorator running')
        self._func()
        print('class decorator ending')

@Foo
def bar():
    print('bar')

bar()

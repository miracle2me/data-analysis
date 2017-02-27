#coding=utf-8

# Generators 生成器,like tuple, generate for once
# () instead of []
mygenerator = (x*x for x in range(4))
# for i in mygenerator:
#     print i

# Yield
def createGenerator():
    mylist = range(4)
    for i in mylist:
        yield i*i

use_generator = createGenerator()
print(use_generator)
# result: <generator object createGenerator at 0x107266c80>
# with yield
for i in use_generator:
    print i
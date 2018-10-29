#__author__:asus
#date:2018/10/29
# class Base(object):
#     def func(self):
#         print('Base,func')
#
# class Foo(Base):
#     def func(self):
#         #方式一：根据mro顺序主动执行父类的方法
#         #super(Foo,self).func()
#         #方式二：主动执行Base类的方法
#         Base.func(self)
#     print('Foo.func')
#
# obj=Foo()
# obj.func()

class Base(object):
    def func(self):
        print("Base.func")

class Bar(object):
    def func(self):
        print("bar.func")

class Foo(Bar,Base):
    pass


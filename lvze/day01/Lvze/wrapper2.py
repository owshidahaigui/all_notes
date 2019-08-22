#类装饰函数

class Add:
    def __init__(self,fun):
        self._fun = fun

    def __call__(self, *args, **kwargs):
        print("a + b:")
        self._fun(*args,**kwargs)
        print("over")

# @Add
# def fun(a,b):
#     print(a + b)
#
# fun(1,2)

# def fun(a,b):
#     print(a + b)
# fun = Add(fun)
# fun(1,2)

# 类装饰类
class Mul:
    def __init__(self,cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        self._cls.begin = 'begin'
        return self._cls(*args,**kwargs)

@Mul
class Foo:
    def __init__(self):
        pass

    def fun(self):
        pass

f = Foo() # Foo = Mul(Foo)   f = Foo()
print(f.begin)


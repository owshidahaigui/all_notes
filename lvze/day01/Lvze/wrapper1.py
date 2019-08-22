# 函数装饰类

def outer(cls):
    def inner(*args,**kwargs):
        cls.begin = "begin"
        obj = cls(*args,**kwargs)
        cls.end = "end"
        return obj
    return inner

@outer
class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

a = MyClass(1,2)

# class MyClass:
#     pass
# inner = outer(MyClass)
# a = inner()


print(a.begin)
print(a.end)
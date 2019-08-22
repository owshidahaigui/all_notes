

#带有参数的装饰器
def outer(*args,**kwargs):
    print("最外层")

    # 我们习惯的装饰器
    def add(func):
        def wrapper(*args, **kwargs):
            print("a + b:")
            result = func(*args, **kwargs)
            print("over")
            return result
        return wrapper

    return add

# add = outer(1000,2000)

# 我们习惯的装饰器
def mul(func):
    def wrapper(*args, **kwargs):
        print("mul 哈哈哈")
        result = func(*args, **kwargs)
        print("mul over")
        return result
    return wrapper

@mul
@outer(1000,2000)
def fun(a,b):
    print(a + b)
fun(1,2)

# def fun(a,b):
#     print(a + b)
# fun = outer(1000,2000)(fun)
# fun = mul(fun)
# fun(1,2)

def fun(a,b):
    print(a + b)
mul(outer(1000,2000)(fun))(1,2) # @语法
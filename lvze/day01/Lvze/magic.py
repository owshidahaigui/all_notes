# 魔法方法的使用
"""
前后有双下划线的方法
__all__ 包中__init__.py
__doc__ 打印说明文档
__name__ 当前文件名
"""

class Magic(object):
    item = {}
    print("class first")
    # 构造方法 真正的创建对象的方法
    def __new__(cls,value):
        print("__new__")
        return object.__new__(cls)

    # 初始化对象 (添加对象属性)
    def __init__(self,value):
        print("__init__")
        self.index = -1
        self.value = range(value)

    # del obj
    def __del__(self):
        print("obj is clear")
    # 重写父类对象打印内容
    def __str__(self):
        return "Magic class"

    # __str__()
    def __repr__(self):
        return "over write str"

    # 让对象可以像函数一样调用，调用时自动启动
    def __call__(self, *args, **kwargs):
        pass

    def __len__(self):
        return 10

    def __sizeof__(self):
        return 10000

    def __iter__(self):
        for i in range(5):
            yield i

    def __next__(self):
        self.index += 1
        if self.index < len(self.value):
           return self.value[self.index]
        else:
            raise StopIteration

    # 属性赋值时调用这个函数
    def __setattr__(self, key, value):
        print("setatter")
        self.__dict__[key] = value

    # 试图使用不能存在的属性时调用这个函数
    def __getattr__(self, item):
        print("getattr")
        self.__dict__[item] = None
        return self.__dict__[item]

    def __getitem__(self,key):
        return self.item[key]

    def __setitem__(self, key, value):
        self.item[key] = value

    def __delitem__(self, key):
        del self.item[key]

m = Magic(4)
# mm = Magic()
# print(m)  # __str__
# del m # __del__

# print(len(m)) # __len__()
# print(m.__sizeof__())
#
# for i in m:
#     print(i)

# m.value = 10
# print(m.abc)

m[0] = 10  # 自动调用 __setitem__()
m[1] = 20
print(m[1]) # 自动调用 __getitem__()
del m[1] # 自动调用 __delitem__()
class Test:
    pass

class Test1(Test):
    def __init__(self):
        super().__init__()

# =====================================
class Test(object):
    pass

class Test1(Test):
    def __init__(self):
        # 第一个参数是当前类,第二个参数是这个类的对象
        super(Test1,self).__init__()
class A:
    pass

class B(A):
    def bar(self):
        print("b")

class C(A):
    def bar(self):
        print("c")

class D(B):
    pass

class E(B):
    pass

class F(D,E,C):
    pass

f = F()
print(F.__mro__) # 继承优先级
f.bar()
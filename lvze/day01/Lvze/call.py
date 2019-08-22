class Call:
    def __init__(self):
        print("__init__")

    def __call__(self, *args, **kwargs):
        print("调用call")
        print(args)


c = Call()
c(1,2)
class Person:
    def __init__(self):
        self.__age = None

    def setAge(self,age):
        if age < 0 or age > 150:
            print("sorry")
        else:
            self.__age = age


Tom = Person()
Tom.setAge(18)

class Color:
    color = 'color'
    @staticmethod
    def value1():
        return Color.color

    @classmethod
    def value2(cls):
        return cls.color

class Red(Color):
    color = "red"

class Green(Color):
    color = "green"

color = Color()
red = Red()
green = Green()
# print(Color.value1())
# print(Color.value2())
print(color.value1())
print(color.value2())
print(red.value1())
print(red.value2())
print(green.value1())
print(green.value2())
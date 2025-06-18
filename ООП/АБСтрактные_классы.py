import abc
from abc import abstractmethod


class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_message(self):
        print(f"X: {self.x} , Y: {self.y}")

    @abstractmethod
    def area(self): pass

#main
#shape = Shape() #Ошибка!
# Нельзя создавать ABC-объект
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14
class Rectagle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x,y)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
#main
rect = Rectagle(1,2,30, 50)
rect.print_message()
print(rect.area())
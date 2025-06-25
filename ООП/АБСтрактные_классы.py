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
class Animal(abc.ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
class Dog(Animal):
    def __init__(self, sound, eat):
        self.sound = sound
        self.eat = eat
    def make_sound(self):
        print(f"Собачка делает {self.sound}")
    def eat(self):
        print(f"Cобачка кушает {self.eat}")
class Cat(Animal):
    def __init__(self, sound, eat):
        self.sound = sound
        self.eat = eat
    def make_sound(self):
        print(f"Кот делает {self.sound}")
    def eat(self):
        print(f"Кот кушает {self.eat}")
class Bird(Animal):
    def __init__(self, sound, eat):
        self.sound = sound
        self.eat = eat
    def make_sound(self):
        print(f"Bird делает {self.sound}")
    def eat(self):
        print(f"Bird кушает {self.eat}")
#MAIN
dog = Dog("ГАВ-ГАВ",'Педигри')
cat = Cat("МЯУ-МЯУ", "Вискас")
bird = Bird("ЧИРИК-ЧИРИК","Семечки")
for animal in [dog,cat,bird]:
    animal.make_sound()
    animal.eat()
# dog.make_sound()
# dog.eat()
# cat.make_sound()
# cat.eat()
# bird.make_sound()
# bird.eat()
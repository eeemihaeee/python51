# # Класс - набор объектов, методов, атрибутов,  - выступащий
# # в роле контейнера(шаблона) для будующего объекта, с кот. работает
# #Уже пользователь
# #Объект - это воплощение требований, характеристик и качеств, кот.
# # приписываются конкретному классу.
# class Car:
#     #Конструктор класса
#     def __init__(self, fuel,maxspeed):
#       self.fuel = fuel
#       self.maxspeed = maxspeed
#     #Функция для заправки топлива
#     def refuel(self, amount):
#         self.fuel += amount
#     #Функция для движения
#     def drive(self):
#         if self.fuel > 0:
#             print("Машина едет.")
#             self.fuel -= 1
#         else:
#             print("Нет топлива!")
#
#
# polo = Car(50, 50)
# mini = Car(10, 90)
# beetle = Car(0, 110)
# print("Сейчас будет двигаться polo")
# for i in range(10):
#     polo.drive()
# print("Сейчас будет двигаться mini")
# for i in range(10):
#     mini.drive()
# print("Сейчас будет двигаться beetle")
# for i in range(10):
#     beetle.drive()
#
#
# #Написать программу "Успеваемость студента." Пользователь вводит
# # 10 оценок от 1 до 5. Реализовать меню для работы:
# #1) Вывод
# #2)Пересдача
# #3)Выходит ли стипендия?
# #4) вывод отсортированных оценок по возрастанию и убыванию
# class Student:
#     def __init__(self,eval_list):
#         self.eval_list = eval_list
#     def menu(self):
#         while True:
#             print("Меню: \n 1) Вывод  \n "
#               "2)Пересдача \n "
#               "3)Стипендия \n "
#               "4) вывод отсортированных оценок по возрастанию и убыванию"
#               "0) Выход")
#             print("*"*11)
#             value = int(input("Ваш выбор: "))
#             if value  == 1:
#                 self.Print() #Вызов Функции Вывода на экран
#             elif value == 2:
#                 self.reEval() #Вызов Функции Пересдачи
#             elif value == 3:
#                 self.ship() #Вызов Функции Вызов стипендии
#             elif value == 4:
#                 self.sort_list() #Вызов Функции Сортировки
#             elif value == 0:
#                 break
#     #Функция замены оценки
#     def reEval(self):
#         self.Print()
#         last_eval = int(input("Введите оценку на ЗАМЕНУ: "))
#         new_eval = int(input("Введите НОВУЮ оценку: "))
#         for i in range(len(self.eval_list)):
#             if self.eval_list[i]  == last_eval:
#                 self.eval_list[i] = new_eval
#                 break
#         print("Оценка изменена!")
#     #Функция вывода на экран
#     def Print(self):
#         print("Список оценок: ",end=' ')
#         for i in self.eval_list:
#             print(i, end=' ')
#         print()
#     def ship(self):
#         if sum(self.eval_list)/len(self.eval_list) >=4:
#             print("Стипендия есть!")
#         else:
#             print("Низкий балл, не видать денешек :( ")
#     def sort_list(self):
#         if int(input("1 - Убывание, 2 - Возрастание \n Ваш выбор: ")) == 1:
#             self.eval_list = sorted(self.eval_list, reverse=True)
#         else:
#             self.eval_list = sorted(self.eval_list)
#         print("Сортировка выполнена! Вот ваш список оценок:")
#         self.Print()
#
# student = Student([1,5,3,4,2,3,5,5,5,5])
# student.menu()


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     #При обращении методом-функцией, котороя обрабатывает строки
#     #Необходимо давать обращение встроему методу __str__, кот.
#     #вернет строку для вывода\обработки
#     def __str__(self):
#         return self.name + " in " + self.galaxy
#
# sun = Star("Sun","Milky Way")
# print(sun)
# #Наследование в ООП
# class Vehicle: #SUPER_CLASS, для ниже стоящих классов
#     pass
# class LandVehicle(Vehicle):#Класс-наследник-подкласс
#     pass
# class TrackedVehicle(LandVehicle):#Класс-наследник-подкласс
#     pass
# # issubclass(OneClass, TwoClass) - функция для определения отношений
# #Между классами, проверка на наследование
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()
# #isinstance(objName, ClassName) = Проверка наличия у объекта
# # определенных характеристик от класса наследника
# myVehicle = Vehicle()
# myLandVehicle = LandVehicle()
# myTrackVehicle = TrackedVehicle()
# for obj1 in [myVehicle, myLandVehicle, myTrackVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj1, cls2), end='\t')
#     print()
# #Пример 2.
# class SampleClass:
#     def __init__(self, value):
#         self.value = value
# obj1 = SampleClass(0)
# obj2 = SampleClass(10)
# obj3 = obj2
# obj3.value += 1
# print(obj1.value, obj2.value, obj3.value)
# #Оператор is позволяет определить, относятся ли две переменные,
# # структуры или объекты к одному объекту класса.
# print( obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)
# #Пример 3. Нахождение методов и атрибутов классов
# class Super:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"Мое имя{self.name}, очень приятно!"
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#
# #MAIN
# obj = Sub("Михаил")
# print(obj)
# #Пример 4.
# class Super:
#     supVar = 1
# class Sub(Super):
#     subVar = 2
#
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)
#
# #Пример 5.
# class Level1:
#     varial = 100
#     def __init__(self):
#         self.var1 = 100
#     def fun1(self):
#         return 102
# class Level2(Level1):
#     varial2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var2 = 201
#     def fun2(self):
#         return 202
# class Level3(Level2):
#     varial3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var3 = 301
#     def fun3(self):
#         return 302
# obj = Level3()
# print(obj.varial, obj.var1, obj.fun1())
# print(obj.varial2, obj.var2, obj.fun2())
# print(obj.varial3, obj.var3, obj.fun3())
# #Пример 6. Множественное наследование
# class SuperA:
#     varA = 10
#     def funA(self):
#         return 11
#     def SetVarA(self,value):
#         self.varA = value
#     def GetVarA(self):
#         return self.varA
# class SuperB:
#     varB = 20
#     def funB(self):
#         return 22
# class SuperC:
#     varC = 30
#     def funC(self):
#         return 33
# class SuperD(SuperA,SuperB,SuperC):
#     pass
#
# #MAIN
# obj = SuperD()
# print(obj.varA, obj.varB, obj.varC)
# print(obj.funA(), obj.funB(), obj.funC())



#Инкапсуляция  - это второй принцип ООП, благодаря кот. классы
# могут скрывать внутренние элементы (атрибуты и функции) от внешнего
#Мира. Реализуется с помощью методов и атрибутов Private and Protected.
#Private - Обозначается с помощью двойного подчеркивания "__" перед именем.
#Доступны только внутри класса, из вне к ним обратиться нельзя.
#Protected - Обозначается с помощью одниночного подчеркивания "_" перед именем.
# условно защищены, но Python не запрещает доступ к ним.
# class BankAccount:
#     def __init__(self, owner, balance):
#         self._owner = owner #Защищенный атрибут
#         self.__balance = balance #Приватный атрибут
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f" Депозит {amount} успешно выполнен.")
#         else:
#             print("Сумма должна быть положительной.")
#     def withdtaw(self, amount):
#         if 0<amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Снятие {amount} успешно.")
#         else:
#             print("Недостаточно средств.")
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, amount):
#         self.__balance = amount
# #MAIN
# acount = BankAccount("Иван Иванов",1000)
# #print(acount.balance) #Ошибка
# print(f"Имя вкладчика: {acount._owner}")
# print(acount.get_balance())
# acount.set_balance(2000)
# acount.withdtaw(200)

# Полиморфизм - 3 столп в ООП, заключается в использовании
# единственной сущности(метода, оператора, объекта)
# для обработки различных типов в различных сценариях.
#Пример 1.
# num1 = 1
# num2 = 2
# print(num1 + num2)
# str1 = 'Python'
# str2 = " 3.13"
# print(str1 + str2)
# #Пример 2. Полиморфизм функций
# print(len("PROGRAMMING"))
# print(len(["A","B","C"]))
# print(len({"Name":"IVAN","AGE":56,"ADDRESS":"PERM"}))
# #Пример 3. Полиморфизм в классах.
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print("Привет, я животное.")
#     def make_sound(self):
#         print("Делаю звуки животного.")
# class Cat(Animal):
#     def __init__(self, name, age):
#         Animal.__init__(self,name, age)
#     def info(self):
#         print(f"Привет, я кошка. Меня зовут {self.name}."
#               f"Мне {self.age} лет.")
#     def make_sound(self):
#         print("Мяууу")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         # self.name = name
#         # self.age = age
#         Animal.__init__(self,name, age)
#     def info(self):
#         print(f"Привет, я собака. Меня зовут {self.name}."
#               f"Мне {self.age} лет.")
#     # def make_sound(self):
#     #     print("Гав-Гав")
# #МЕЙН
# dog = Dog("Шарик", 10)
# cat = Cat("Мурка", 6)
# for animals in [dog,cat]:
#     animals.make_sound()
#     animals.info()
#     animals.make_sound()
#Пример 4. Переопределение методов
# from math import pi
# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         pass
#     def fact(self):
#         return "Я фигура для подсчета."
#     def __str__(self):
#         return self.name
# class Square(Shape):
#     def __init__(self, lenght):
#         self.lenght = lenght
#         Shape.__init__(self,"Square")
#     def area(self):
#         return self.lenght**2
#     def fact(self):
#         return "У меня все углы 90 градусов."
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         Shape.__init__(self,"Circle")
#     def area(self):
#         return pi*self.radius**2
# #MAIN
# a = Square(4)
# b = Circle(5)
# print(b.fact())
# print(a.fact())
# print(b.area())
# print(b)
# print(a)
#Перегрузка(переопределение) методов в классе
#Cложение a + b __add__(a,b)
#Объединение seq1 + seq1 __concat__(seq1, seq2)
#Проверка наличия obj in seq __constins__(seq, obj)
#Деление a / b __truediv(a,b)
#Поразрядное И a & b __add__(a,b)
#Поразрядное ИЛИ a ^ b __xor__(a,b)
#Поразрядная инверсия ~a   __invert__(a)
#Поразрядное И ИЛИ a | b __or__(a, b)
#Степень a ** b __pow__(a, b)
#Присвоение по индексу obj[k] = a __setitem__(obj, k, a)
#Удаление по индексу del obj[k] __delitem__(obj, k)
#Обращение по индексу obj[k] __getitem__(obj, k)
# остаток от деления a % b __mod__(a,b)
#Пример 6. Создайте класс Circle(окружность).
# Для данного класса реалуйте ряд перегруженных методов:
#1) Проверка на равенство ради усов двух окружностей (==)
#2) Сравнение длин двух окружностей (<,>,<=,>=)
#3) Пропорциональное изменение размераов окружностей,
#путем изменение радиуса (+ ,- ,+= ,-=)
import math
class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
    def circleference(self): #Длина окружности
        return 2* math.pi *self.radius
    def __eq__(self, other): #Cравнение объектов по длине
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius
    def __gt__(self, other): #
        return self.circleference() > other.circleference()
    def __lt__(self, other): #
        return self.circleference() < other.circleference()
    def __le__(self, other): #
        return self.circleference() <= other.circleference()
    def __ge__(self, other): #
        return self.circleference() >= other.circleference()
    def __add__(self, other): # Cумма
        return Circle(self.radius + other.radius)
    def __str__(self): #обработка вызова print
        return f"Circle radius={self.radius}"
    def __sub__(self,other):
        return Circle(self.radius - other.radius)
    def __iadd__(self, value):
        self.radius += value
        return self
    def __isub__(self,value):
        self.radius -= value
        return self
#MAIN
circle1 = Circle(5)
circle2 = Circle(7)
print( circle1 == circle2)
print(circle1 > circle2)
circle3 = circle1+circle2
print(circle3)
circle4 = circle1 - circle2
print(circle4)
circle1 += 3
print(circle1)
circle2 -= 10
print(circle2)







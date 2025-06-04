# Задача 1.
# Создайте класс Soda (для определения типа газированной воды),
#  принимающий 1 аргумент при инициализации
#  (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(),
#  выводящий на печать «Газировка и {ДОБАВКА}»
#  в случае наличия добавки, а иначе отобразится
#  следующая фраза: «Обычная газировка».
import random


class Soda:
    def __init__(self,dobavka = None):
        self.dobavka = dobavka
        self.show_my_drink()
    def show_my_drink(self):
        if self.dobavka == None:
            print("«Обычная газировка»")
        else:
            print(f'Газировка с {self.dobavka}')
#MAIN
soda1 = Soda()
soda2 = Soda("Карамель")
#soda1.show_my_drink()
#soda2.show_my_drink()
# Рассмотрим объект «Программист», который задаётся именем,
# должностью и количеством отработанных часов.
# Каждая должность имеет собственный оклад (заработную плату за час работы).
# В нашей импровизированной компании существуют 3 должности:
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик
# за каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем
# и должностью (отработка у нового работника равна нулю).
# Класс реализует следующие методы:
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате:
# <имя> <количество отработанных часов>ч. <накопленная зарплата> тгр.cl
class Programist:
    def __init__(self, name, rank):
        self.name = name
        self.time = 0
        self.rank = rank
        self.state = 0
        match (self.rank):
            case "Junior":
                self.state = 10
            case "Senior":
                self.state = 20
            case "Middle":
                self.state = 15
    def work(self, value):
        self.time += value
        print("Часы записаны!")
    def rise(self):
        match(self.rank):
            case "Junior":
                self.rank = "Middle"
                self.state = 15
            case "Senior":
                    self.state += 1
            case "Middle":
                self.rank = "Senior"
                self.state = 20
    def info(self):
        return f"{self.name} {self.time}ч. {self.time * self.state} тугриков"
import random
class NPC:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def __str__(self):
        return f"Я {self.name}, у меня {self.hp} HP"
    def attack(self):
        pass
class Swordsman(NPC):
    def __init__(self, name1, hp1,min_damage, max_damage):
        NPC.__init__(self,name1, hp1)
        self.min_damage = min_damage
        self.max_damage = max_damage
    def attack(self):
        return f"Мечник нанес {random.randint(self.min_damage, self.max_damage)}"
class Mage(NPC):
    def __init__(self, name2, hp2,mana):
        NPC.__init__(self,name2,hp2)
        self.mana = mana

    def attack(self):
        if self.mana > 0:
            s = f"Маг нанес {self.mana*2}"
            self.mana -= 20
            return s
        else:
            return f"Маг без маны. Не может атаковать"

mage = Mage("Гендальф", 50, 100)
print(mage)
for i in range(6): print(mage.attack())
swordsmen = Swordsman("Арагорн0", 150, 1, 20)
print(swordsmen)
for i in range(2):
    print(swordsmen.attack())

class MSDice:
    def __init__(self, gran):
        self.gran = gran
    def PR(self):
        return f"Кубик D{self.gran}, выпало: {random.randint(1,self.gran+1)}"
class Player:
    def __init__(self, nickname):
        self.inventory = []
        self.nickname = nickname
        self.exp_points = 0
    def __str__(self):
        return f"Имя: {self.nickname}, опыт:{self.exp_points}, инвентарь: {self.inventory}"
    def addExp(self, value):
        self.exp_points += value
        print(f"{value} Опыта получено!")
    def addItem(self, item):
        self.inventory.append(item)
        print(item," Добавлен")
    def removeItem(self, item):
        self.inventory.pop(item)
        print(item, " Удален.")
class Resistors:
    def parallel(self, r1, r2):
        return r1*r2 / (r1+r2)
    def consec(self, *args):
        result = 0
        for i in args:
            result += i
        return result
#MAIN
resistors = Resistors()
resistors.consec(1,5,8,5,3,2,6,8,8)
resistors.parallel(20,40)

#Класс-Родитель для всех классов в игре
import random


class Class_Hero:
    def __init__(self, Speed,Intelligence, Strength, Agility, Luck,Attack_Power):
        self.Speed = Speed
        self.Intelligence = Intelligence
        self.Agility = Agility
        self.Luck = Luck
        self.Attack_Power = Attack_Power
        self.Strength = Strength
        self.Actions = [self.Jump,self.Move, self.Attack, self.Deffence]
    def Jump(self):
        pass
    def Move(self):
        pass
    def Attack(self):
        pass
    def Deffence(self):
        pass
#NPC - Базовый класс с параметрами для игровых персонажей и врагов
class NPC:
    def __init__(self, Attack_Power, HP):
        self.Attack_Power = Attack_Power
        self.HP = HP
class Enemy(NPC):
    def __init__(self):
        self.enemy_list = ['Гоблин','Куб-Слизь','Дракон','Повелитель телей']
        NPC.__init__(self, random.randint(50,100),random.randint(100,200))
        self.Enemy_Name = self.enemy_list[random(len(self.enemy_list)-1)]
#Класс для реализации Лучника
class Archer(Class_Hero,NPC):
    def __init__(self,Speed = 1,Intelligence =2, Strength=1, Agility=5, Luck=1,Attack_Power=5):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        self.Ability = [self.Shot_Arche, self.Dodge,self.Ultimate] #Список способностей
    def Shot_Arche(self):
        pass
    def Dodge(self):
        pass
    def Ultimate(self):
        pass
#Класс для реализации Целителя
class Healer(Class_Hero):
    def __init__(self,Speed = 0,Intelligence =5, Strength=0, Agility=2, Luck=0,Attack_Power=1):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        self.Ability = [self.Attack_middle, self.Heal, self.Ultimate]  # Список способностей
    def Heal(self):
        pass
    def Attack_middle(self):
        pass
    def Ultimate(self):
        pass
#Класс для реализации Мага
class Mage(Class_Hero):
    def __init__(self,Speed = 3,Intelligence =10, Strength=0, Agility=8, Luck=3,Attack_Power=8):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        self.Ability = [self.FireBoll, self.Magic_Shild, self.Ultimate]  # Список способностей
    def FireBoll(self):
        pass
    def Ultimate(self):
        pass
    def Magic_Shild(self):
        pass
#Класс для реализации Воина
class Warrior(Class_Hero):
    def __init__(self,Speed = 4,Intelligence =-1, Strength=10, Agility=1, Luck=3,Attack_Power=8):
        Class_Hero.__init__(self,Speed,Intelligence, Strength, Agility, Luck,Attack_Power)
        self.Ability = [self.Attack_Sword, self.Deffence_Shild, self.Ultimate]  # Список способностей
    def Ultimate(self):
        pass
    def Deffence_Shild(self):
        pass
    def Attack_Sword(self):
        pass


#Класс-Меню_Выбора_Персонажа
class Game_Select_Hero:
    def __init__(self):
        self.name = ''
    def Hero_Select_User(self):
        self.name = input("Введите Имя:")
#Класс-Меню_Игрового_Процесса
class Game_Process_Change:
    gameSelectHero = Game_Select_Hero() #Создаем конструктор для пользователя
    gameSelectHero.Hero_Select_User()
    Hero = Warrior(gameSelectHero.name)



#MAIN Для запуска
def main():
    pass
if __name__ == "__main__":
    main()

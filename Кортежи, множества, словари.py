#Кортеж - неизменяемая структура данных,
#кот. по своему подобию похожа на список.
# Список - изменяемый тип данных [1,2,3]
#a = [1,2,3]
#a[1] = 5
#print(a)
#b = (1,2,3)
#b[1] = 15 # ошибка TypeError
#print(b)
#Плюсы:
#1) Экономия места
#2) в процессе работы, данные в безопасности
#3) Выше производительность программы
from itertools import islice

a = (1,2,3)
print(type(a)) #class typle
print(a[1]) #2
del a
lst = [1,2,3,4,5]
print(type(lst))
print(lst)
tpl = tuple(lst)
print(type(tpl)) #tuple
print(tpl)
#обратно
lst2 = list(tpl)
print(type(lst2))
print(lst2)
#Словари (dict)
#Словарь - неупорядоченная структура данных, кот.
# позволяет хранить в себе данные в формате пар:
# "Ключ": "Значение"
dictionary = {"Персона":"Человек",
              "Марафон":"Гонка бегунов длиной около 26 миль",
              "Айфон":15,
              }
dictionary2 = {(1,1.2,0.2):"Кортежи могут быть ключами",
               1 :"Целые числа могут быть ключами",
               "БЕЖАТЬ":"строки тоже",
               ['носок',1,5]:"а списки не могут"
               }
#не работают нехэшируемые типы данных
dictionary3 = {True:'yes',1:'no',1.0:'maybe'}
#Работа со словарями
d = {}
d = {'dict_key':'dict_value'}
d = dict(short='dict', long='dictionary')
d['index'] = 20
d = dict.fromkeys(['a','b'],100)
key_list = ['marvel','dc']
value_list = ['Spiderman','Flash']
superhero_list = dict(zip(key_list, value_list))
d = {i : i**2 for i in range(10)} #Генератор словарей
print(d)
#Получение данных из словаря
dictionary4 = {"Марафон":26}
print(dictionary4['Марафон']) #Получение значений
#/Ошибка, если ключа не существует
#Для лучшего исхода лучше использовать метод *.get()
# для удаления данных используется метод del dictionary4['Марафон']
# d.clear() #очищает словарь от всех пар, но не удаляет переменную
# d.copy()
# d = dictionary
#id(d)#12345678
#id(dictionary)#12345678
#dictionary4.get('Марафон') #26
#d.update() #Обновление нескольких пар ключей сразу
#dictionary = {"Персона":"Человек",
#              "Марафон":"Гонка бегунов длиной около 26 миль",
#              "Айфон":15,
#              }
#dictionary.update("Марафон":"33км","Айфон":11)
#d.pop(key) #удаляет ключ и возвращает его значение
#d.setdefault("name") #Ищет ключ и возращает его значение, если
# он не найдет - создает этот ключ со значением None
#d.keys() #возвращает список ключей в словаре
#d.values() #Возвращает список значений словаря
#d.items() #возращает пары ключ:значение
#Примеры
#1. Итерация через консоль
story_dict = {"Сто":100,"Двести":200,"Тристо":300}
for key in story_dict:
    print(key)
for key,value in story_dict.items():
    print(key, value)
#Сортировка
people = {3:'jim',
          4:'olga',
          1:'max',
          5:'ivan',
          6:'kirill'}
print(sorted(people))
import itertools
#Если задача состоит в том, что словарь слишком большой,
# а вам нужна лишь его часть - вам поможет метод islice()
nd = dict(itertools.islice(people.items(), 0, 3))
print(nd)
#dict to list
people_list = []
for key, value  in people.items():
    temp = [key, value]
    people_list.append(temp)
#p_l = [[key,value] for key, value in people.items()]

#Множества(set) - контейнер, содержащий не повторяющиеся
# элементы в случайном порядке
#Создание множества
s = set()
print(type(s)) #class set
s = set('hello')
#{'h','e','l','o'}
s = {i **2 for i in range(10)}
print(s)
#Методы set
# len()
# x in s #Проверка принадлежности
#s.isdisjoint(other) - истина, если set и other
# не имеют общих элементов
# set == other -проверка всех элементов множества
# на пересечение с другим множеством
# s.issubset(other) - проверка принадлежности множества
# s.issuperset(other) - проверка 2множества на вхождение в 1
# s.union(other,...) #объединение нескольких множеств
# s.intersection(other) - пересечение множеств
# s.difference() - множество элементов, уникальных в 2х множествах
# s.symmetric_difference() - уникальные встречающиеся элементы
# s.copy()
# s.update(other)
# s.intersection_update(other)
# s.difference_update(other)
# s.simmetric_difference_update(other)
# s.add(item) - добавление элемента
# s.remove(item) - удаление
# s.discard(item) - удаление элемента, если он есть в множестве
# s.pop() - удаляет случайный элемент
# s. clear() - очистка множества
# Пример "Задача инвестора".
our_products = {"Apple","Tesla","DNS"}
range_of_company_1 = {"Samsung","Sony"}
range_of_company_2 = {"Apple","BMW","IBM"}
range_of_company_3 = {"BMW","Tesla","DNS","Ferrary"}
#Акции, которые уже у нас есть в 3х списках
print("Акции, которые уже у нас есть в 3х списках:")
print(our_products.intersection(range_of_company_1))
print(our_products.intersection(range_of_company_2))
print(our_products.intersection(range_of_company_3))
#Противоположная задача
print("Акции, которых нет у нас есть в 3х списках:")
print(our_products.difference(range_of_company_1))
print(our_products.difference(range_of_company_2))
print(our_products.difference(range_of_company_3))
#Разница в товарах
print("Разница в 3х списках:")
print(our_products.symmetric_difference(range_of_company_1))
print(our_products.symmetric_difference(range_of_company_2))
print(our_products.symmetric_difference(range_of_company_3))
frozenset_product = frozenset(our_products) #Замороженный портфель
#Пример 2 "Журнал Юзера"
my_dict = {"Nikita":{
                        "Tel": "12345678910",
                        "OK":"ok.ru/nikita41",
                        "Vk":"vk.com/nikitaaa",
                        "Nick":"Друг детства"
                    },
           "Marina":{},
           "Max":{}
           }
user = my_dict[input("Введите имя пользователя:")][input("Что конкретно? -->")]
print(user)

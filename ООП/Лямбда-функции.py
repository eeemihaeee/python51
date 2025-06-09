# Лямбда-функции = это функции,
#кот. используют след. синтаксис:
# lambda parametes: expression
# parametes - перечень параметров,
# через запятую
# expression - действие с этими параметрами
#нельзя использовать циклы,
# условные операторы,
# return
from pyexpat.errors import messages

x1 = 1
s = lambda x:"1" if x==1 else "Lambda"
print(s(2))
#Пример 2
def area(h,a):
    return h*a
a = area(5,10)
b = lambda h,a: h*a
print(b(5,10))
#Пример 3.
# Сортировка по ключу
elements = [(2,12,'Mg'),(1,11,'Na'),(1,3,"Li"),(2,4,"Be")]
#sorted(elements)
print(elements)
#elements.sort(key=lambda e: (e[1],e[2]))
elements.sort(key=lambda e: e[-3:-1])
print(elements)
#Пример 4. Словари со значением по умолчанию
import collections
#Вызов значения по умолчанию, при отсутствии элементов внутри контейнера
mimus_one_dict = collections.defaultdict(lambda :-1)
point_zero_dict = collections.defaultdict(lambda :(0,0))
messages_dict = collections.defaultdict(lambda : "No message")
print(mimus_one_dict[1], point_zero_dict[(1,2)], messages_dict[''], sep='\n')
print(mimus_one_dict, point_zero_dict, messages_dict, sep='\n')
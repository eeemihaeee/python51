# Задание 1
# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.
import random
def my_sort_one(mass):
    for j in range(value):
        for i in range(value):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1]= mass[i+1],mass[i]

def my_sort_two(mass, value):
    for j in range(value):
        for i in range(value):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1]= mass[i+1],mass[i]

mass = [random.randint(-10,10) for i in range(10)]
sr_z = sum(mass)/len(mass)
if sr_z < 0:
    value = (len(mass) // 3)*2
    my_sort_one(mass,value)
else:
    value = len(mass)//3
    my_sort_two(mass,value)
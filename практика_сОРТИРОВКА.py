# Задание 1
# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.
import random
# def my_sort_one(mass):
#     for j in range(value):
#         for i in range(value):
#             if mass[i] > mass[i+1]:
#                 mass[i],mass[i+1]= mass[i+1],mass[i]
#
# def my_sort_two(mass, value):
#     for j in range(value):
#         for i in range(value):
#             if mass[i] > mass[i+1]:
#                 mass[i],mass[i+1]= mass[i+1],mass[i]
#
# mass = [random.randint(-10,10) for i in range(10)]
# sr_z = sum(mass)/len(mass)
# if sr_z < 0:
#     value = (len(mass) // 3)*2
#     my_sort_one(mass,value)
# else:
#     value = len(mass)//3
#     my_sort_two(mass,value)


#Есть стопка оладий различного радиуса. Единсвенная
#операция, проводимая с ними - между двумя любыми оладиями
#просовываем лопатку и меняем порядок оладий на обратный.
#Необходимо за минимальное кол-во операций таких отсортировать
#снизу вверх по убыванию радиуса оладья.
def pancakes_sort(mass):
    #Поиск индекса максимального элемента
    def find_largest_index(mass, n):
        i = 0
        for j in range(n):
            if mass[j] > mass[i]:
                i = j
        return i
    #Функция переворачивания блинчика
    def flip(mass, k):
        return mass[:k][::-1] + mass[k:]
    result = []
    n = len(mass)
    while n > 1:
        i = find_largest_index(mass, n)
        if i < n-1:
            mass = flip(mass, i+1)
            result.append(i+1)
            mass = flip(mass, n)
            result.append(n)
        n -= 1
    return result
pancakes = [3,1,4,5,9,6,4,3,6,2,4,7]
oper = pancakes_sort(pancakes)
print(f"Оладья: {pancakes}")
print(f"Операции: {oper}")

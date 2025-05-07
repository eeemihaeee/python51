import random
#Пузырьковая сортировка
def bubble_sort(mass):
        #Для выполния алгоритма, необходмо сравнивать 2 элемента
        # массива друг с другом, если первый элемент больше второго,
        # то мы их меняем местами. Процесс продолжается до послей
        # Пары элементов сравнения. Алгорим повторяется n^2 раз,
        #даже, если массив уже отсортирован.
        swapped = True #Нужна для запуска сортировки 1 раз.
        while swapped:
            swapped = False
            for i in range(len(mass) - 1):
                if mass[i] > mass[i+1]: #Проверка элементов
                    mass[i],mass[i+1] = mass[i+1],mass[i] #Свап
                    swapped = True #Возвращаем значение для
                                   # дальнейших иттераций
#Сортировка выборкой - делит список на две части: отсортированную ъ
# и неотсортированную. В качестве него используется крайняя левая
# часть списка. Находится наименьший элемент и меняется
# с первым элементом местами.
def selection_sort(mass):
    for i in range(len(mass)):
        # i - значение соответствует кол-во отсортированных
        # элементов в списке
        lowest_value_index = i #исходно считаем наименьшим первый элемент
        for j in range(i+1, len(mass)):
            if mass[j] < mass[lowest_value_index]:
                lowest_value_index = j
        mass[i], mass[lowest_value_index] = mass[lowest_value_index],mass[i]
#Метод сортировки вставками - работает по тому же принципу, как и сортировка выборкой:
#Делит список на 2 части. Алгоритм перебирает второй сегмент и вставляет текущий
# элемент в правильную позицию.
# Предполается ,что первый элемент списка уже отсортирован. Переходим к след. элементу, обозначим его как х.
# Если х больше первого элемента, оставляем его на своем месте.
# Если он меньше, копируем его на вторую позицию, а х устанавливаем как первый элемент
# Переходя к другим элементам несортированного списка, перемещаем более крупные элементы
# в отсортированный вверх по списку,
#Пока не встретим элемент меньше х или не дойдем до конца. В первом случае,
# х помещается на правильную позицию.
def insert_sort(mass):
    for i in range(1, len(mass)): #Наинаем сортировку со 2 элемента, т.к. считаем,
        # что первый элемент уже отсортирован
        item_to_insert = mass[i]
        #Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        while j>= 0 and mass[j] > item_to_insert:
            mass[j+1] = mass[j]
            j -= 1
        mass[j + 1] = item_to_insert
#Пирамидальная сортировка - сортировка кучей. Работает как 2 выше написанных алгоритма,
# преобразует второй элемент списка в структуру данных "куча"(heap), чтобы можно было
# эффективно определить самый большой элемент.
#
def heapify(mass, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    #Если левый потом корня - допустимый индекс, а элемент больше, чем текущий наибольший,
    # обновляем элемент
    if left_child < heap_size and mass[left_child] > mass[largest]:
        largest = left_child
    #тТочно также проверяем правый корень
    if right_child < heap_size and mass[right_child] > mass[largest]:
        largest = right_child
    #Если наибольший элемент больше не является корнем дерева, то они меняются местами
    if largest != root_index:
        mass[root_index], mass[largest] = mass[largest],mass[root_index]
        heapify(mass, heap_size, largest)
def heap_sort(mass):
    n = len(mass)
    for i in range(n, -1, -1):
        heapify(mass, n, i)
    #Перемещаем корень Max Heap в конец списка
    for i in range(n-1, 0, -1):
        mass[0], mass[i] = mass[i],mass[0]
        heapify(mass, i, 0)
        
#MAIN
random_mass= [random.randint(1,10) for i in range(10)]
print("Сортировка Пузырьком:")
print(f"Исходный: {random_mass}")
bubble_sort(random_mass)
print(random_mass)
random_mass= [random.randint(1,10) for i in range(10)]
print("Сортировка Выборкой:")
print(f"Исходный: {random_mass}")
selection_sort(random_mass)
print(f"Сортировка: {random_mass}")
random_mass= [random.randint(1,10) for i in range(10)]
print("Сортировка Вставками:")
print(f"Исходный: {random_mass}")
insert_sort(random_mass)
print(f"Сортировка: {random_mass}")

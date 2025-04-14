# if (условие):
    #действие
# elif(условие):
    #дейстивие
# elif(условие):
    #дейстивие
# elif(условие):
    #дейстивие
#else:
    #действие
# value = int(input("Введите число:"))
# if value > 0:
#     print("Число положительное!")
# elif value == 0:
#     print("Число равно нулю!")
# else:
#     print("Число отрицательное!")
# value1 == value2
# value1 != value2
# value > 0
# value < 0
# value >= 0
# value <= 0
# age = int(input("Введите ваш возраст:"))
# if age < 10 and age > 0:
#     print("Вы еще малыш!")
# elif age >= 10 and age < 21:
#     print("Вы подросток!")
# elif age >=21 and age < 45:
#     print("Вы молодеж!")
# elif age >=45 and age < 100:
#     print("Вы пенсионер!")
# else:
#     print("Некорректное значение возрастра!")
# time = int(input("Введите значение текущего времени в часах:")) % 24
# ticket = False
# money = True
# luggage =False
#print(money or ticket and not luggage and time > 6)
#car_speed = 50
#if ((car_speed >= 50) or (car_speed <= 120)) and car_speed != 200:
 #   print("Машина двигается быстро! Снизьте скорость!")
#Исключения. Обработка событий ошибки
# try:
#     amount = int(input("Введите число предметов:"))
#
# except ValueError:
#     print("Ошибка! Введите только число!!!")
# value = int(input("Введите число1"))
# value2 = int(input("Введите число2"))
# try:
#     print(f"Деление {value / value2}")
# except ZeroDivisionError:
#     print("Делить на 0 нельзя!")
# finally:
#     print("Действие с делением было выполнено!")
#Практика
#Задание 1.
#Пользовать вводит с клавиатуры число. Нужно проверить его на
#четность/нечетность. Если четное - вывести even, обратно - odd
# value = int(input())
# if value % 2 == 0:
#     print('even')
# else:
#     print('odd')
#ЗАдание 2. Пользователь вводит число. Нужно проверить его
#на кратность 7. вывести надпись : Number is multiple 7,
#иначе : number is not multiple 7
#Задание 3. Пользователь вводит 2 числа. Нужно проверить их
#И найти максимум(наибольшее). Вывести его на экран.
#Задание 4. Пользователь вводит 2 числа. Нужно проверить их
#И найти минимум(наименьшее). Вывести его на экран.
#Задание 5. Пользователь вводит 2 числа. В зависимости от
# выбора пользователя, необходимо показать сложение чисел,
# #РаЗность чисел, произведение, деление, сред. арифметическое.
# value1 = int(input())
# value2 = int(input())
# userCh = int(input("Выбери действие : 1)Сложение"
#                    " \n2)Вычитание \n3)Умножение \n4)Деление"
#                    "\n Ваш выбор: "))
# if userCh == 1:
#     print(value1 + value2)
# elif userCh == 2:
#     print(value1 - value2)
# elif userCh == 3:
#     print(value1 * value2)
# elif userCh == 4:
#     try:
#         print(value1 / value2)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
# else:
#     print("Введены не те данные!")
#

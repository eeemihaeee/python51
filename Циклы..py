#for (УСЛОВИЕ):
    #ОПЕРАЦИЯ
# for i in range(10,100):
#     print("*" * i)
#     i = 2
# sum = 0
# value = int(input("Введите число для ввода данных:"))
# for i in range(value):
#     sum = sum + int(input("Введите число: "))
#     print(i)
# del i
# print(i)
# print(f'Сумма чисел пользователя: {sum}')
# for i in range(10):
#     print('%' * i, end=' ')
#     for j in range(10):
#         print("*",end=' ')
    #print('\n')
#Цикл while
#while (Условия):
    #программа, инструкции
# while True:
#     try:
#         age = int(input("Введите свой возраст: "))
#     except ValueError:
#         print("Введите корректное значение!")
#         continue #завершает текущую итерацию, игнорирует
#         # внутренний код и начинает новый виток цикла
#     break #используется как точка выхода из цикла
# print(f"Вы ввели свой возраст - {age}, вы старый!")
# i = 0
# while i <= 10:
#     print(i**2)
#     i += 1
# f = 1
# valueUser = int(input("Введите значение для факториала:"))
# i = 1
# while i <= valueUser:
#     f *= i
#     print(f" Шаг {i}, значение факториала равно:{f}")
#     i += 1
# # print(f"ваш факториал равен: {f}")
# #Проверка строки на палиндром через цикл while
# stringUser = input("Введите строку для проверки:")
# #А роза упала на лапу Азора
# #а буду я у дуба
# i = len(stringUser) - 1
# strA = ''
# while i >= 0:
#     strA += stringUser[i]
#     i -= 1
# if strA == stringUser:
#     print("Строка палиндром!")
# else:
#     print("Строка - не палиндром!")
# strA = ''
# for i in stringUser:
#     strA = i + strA
# if strA == stringUser:
#     print()
# if stringUser == stringUser[::-1]:
#     print("Строка палиндром!")
#Метод среза строки
# stringA = "Hello world"
# a = stringA[6] # 'w'
# b = stringA[0:5]# 'Hello'
# c = stringA[0:5:2] #'Hlo'
# d = stringA[0:5:-1]#'olleH'
#stringB = "".join(reversed(stringA))
#stringC = ",".join(reversed(stringA)) #'H,e,l,l,o'
#stringB = " ".split(reversed(stringA))
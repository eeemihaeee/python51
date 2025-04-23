# import random
# import datetime
# print("Добро пожаловать в игру <Угадай число!>")
# print("Правила очень просты: ты пытаешься угадать число"
#       "от 1 до 500, я даю тебе подсказки!")
# print("*"*11)
# user_choice_count = 0
# user_choice_time = datetime.datetime.now() #текущее время
# print(f"Начало игры в {user_choice_time}")
# random_value = random.randint(1,500)
# #randint - функция для выбора
# # случайного числа в интервале
# while True:
#     user_choice_count += 1
#     value_user = int(input("Введите предполагаемое"
#                            " число: "))
#     if value_user == random_value:
#         print("Вы угадали число! Поздравляю!")
#         break
#     elif value_user < random_value:
#         print("Ваше число меньше загаданного")
#     elif value_user > random_value:
#         print("Ваше число больше загаданного")
#     print("*"*11)
# delta_time = datetime.datetime.now() - user_choice_time
# print(f"Статистика: \n Попыток ->{user_choice_count} \n Время->{delta_time}")
#


#value1, value2 = input("111"), input("222")
value1 = int(input())
value2 = int(input())
number = int(input())
for i in range(value1, value2+1):
    if i == number:
        print(f"!{i}!", end=' ')
    else:
        print(i, end=' ')
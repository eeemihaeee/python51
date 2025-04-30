import math as mt, sys
from config import *
# from platform import (platform,machine, processor,
#                       system, version)
# #print(mt.pi)
# #print(user_value)
#
# #for name in dir(mt):
#  #   print(name, end='\t')
# print(system())
# print(version())
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print(machine())
# print(processor())
#
# def plus(c,d):
#     return f"{c}+{d}={c + d} \n"
# def minus(a,b):
#     return f"{a}-{b}={a - b} \n"
# def delet(a,b):
#     return f"{a}/{b}={a / b} \n"
# def umnoj(a,b):
#     return f"{a}*{b}={a * b} \n"
# def calcul():
#     a = int(input("Value1:"))
#     b = int(input("Value2:"))
#     print(plus(a,b) + umnoj(a,b) + delet(a,b) + minus(a,b))
#
# #MAIN
#
#
# if __name__ == "__main__":
#     calcul()

#Напишите функцию, которая отображает фразу:
# "Не сравнивайте себя ни с кем. Это оскорбительно в первую очередь для вас".
#Билл Гейтс
def print_f():
    print("Не сравнивайте себя ни с кем. Это оскорбительно" \ 
    "в первую очередь для вас. \n Билл Гейтс")
print_f()
#2 числа и четные числа
def chet(a,b):
    if a > b:
        a,b = b,a
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i,end=' ')
    print()
value1 = int(input())
value2 = int(input())
chet(value1,value2)

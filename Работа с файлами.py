#Файл - это всего лишь набор данных
# Представленных в видие последовательности
# битов на ПК, информация хранится в
#куче данных(структуре данных) и
# имеет название "Имя файла".
# В python есть 2 типа данных:
# 1) Текстовые *.txt, *.rtf
# 2) Бинарные *.bin
#Последовательность операций:
#1) Открытие файла
#2) Выполнение операции(чтение, запись)
#3)Закрытие потока

f = open('test.txt',"r")
# r - только для чтения.
# w - только для записи. Если файла нет, он его создаст
# rb - только для чтения(бинарный файл)
# wb - только для записи(бинарный файл)
# r+ - для чтения и записи
# a - открытие файла для редактирования. так же создает
# новый файл, если он не найден
# rb +, wb+, a+, ab, ab+
print(*f) # * - распаковка любого типа данных
f.close() #закрытие потока работы с файлом

f = open('test.txt',"r")
try:
    print(*f)
finally:
    f.close()

with open('test.txt','r') as f:
    print(f.read(10)) #чтение определенного кол-во символов в файле
    print(f.readline(0)) #Функция работы со строками
    print(f.readline(1))
    print(f.readlines())
    #print(*f)
#Запись в файл
with open("practic.txt",'w') as f:
    f.write("Per aspera ad astra")
#Чтение из файла
with open("practic.txt",'r') as f:
    print(f.readlines())
# file.fileno() - проверка целостности файла
# file.flush() - очистка буфера обмена файла(поток)
# file.isatty() - Возращает True, если файл закреплен для работы с терминалом
# file.next() - возвращает след. строку из файла
# file.seek() - устанавливает текущую позицию указателя в файле
# file.seekable() - проверяет доступ к файлу, случайный доспут
# file.tell() - возращает текущюю позицию в файле
# file.truncate(n) - уменьшает размер файла,
# если n указана, то файл обрезается до n-байт, если нет
# - то до текущей позиции
# file.writelines() - добавляет последовательность строк в файл
import os
os.rename('test.txt','test123.txt')
#Пример реализации приложения "Шпионаж".
def file_collector(path): #фУНКЦИЯ ДЛЯ ЗАПИСИ В ФАЙЛ
    path = os.path.normpath(path) #НОРМАЛИЦИЯ ПУТИ
    result = {"dirs":[],"files":[]} #ФИНАЛЬНЫЙ СЛОВАРЬ ВСЕХ ФАЙЛОВ И ПАПОК
    for path, dirnames, filenames in os.walk(path):#ПРОХОДИМСЯ ПО ПУТИ
        for dir in dirnames: #ПЕРЕБИРАЕМ ВСЕ ПАПКИ
            result['dirs'].append(dir) #ДОБАВЛЯЕМ ИХ В СЛОВАРЬ
        for file in filenames: #ПЕРЕБИРАЕМ ВСЕ ФАЙЛЫ
            result['files'].append(file) #ДОБАВЛЯЕМ ИХ В СЛОВАРЬ
    file = open("collector.txt",'w') #СОЗДАЕМ ФАЙЛ ДЛЯ ЗАПИСИ
    file.write("*"*4+f"Directories"+"*"*4) #ЗАГОЛОВОК
    for dir in result['dirs']: #ЗАПИСЫВАЕМ ВСЕ ДАНННЫЕ ИЗ СЛОВАРЯ
        file.write(f'\n {dir}\n')
    file.write("*" * 4 + f"Files" + "*" * 4)#ЗАПИСЫВАЕМ ВСЕ ДАНННЫЕ ИЗ СЛОВАРЯ
    for file in result['files']:
        file.write(f'\n {file}\n')
    file.close()#ЗАКРЫТИЕ ПОТОКА
path='C:\Program Files' #Путь, который есть на этом ПК
file_collector(path)#ВЫЗОВ ФУНКЦИИ


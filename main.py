#print("Hello world!!!")
#Функция для печати текста
# и его вывода в консоль
# name = input("Введите ваше имя: ")
# age = input("Введите ваш возраст: ")
# print("Привет," , name , " Тебе ",age ," лет")

#Калькулятор
# value1 = int(input("Введите первую переменную:"))
# value2 = int(input("Введите вторую переменную:"))
# print(f"{value1} + {value2} = {value1 + value2}")#сумма элементов
#string - тип данных для текста
#int - тип данных для целочисленных чисел
#float - тип данных с плавающей точкой
#bool - тип данных логический, True, False
# print(f"{value1} - {value2} = {value1 - value2}")
# print(f"{value1} * {value2} = {value1 * value2}")
# print(f"{value1} / {value2} = {value1 / value2}")
# print(f"{value1} // {value2} = {value1 // value2}")
# print(f"{value1} % {value2} = {value1 % value2}")
# print(f"{value1} ** {value2} = {value1 ** value2}")
# print("*" * 11)
#Проверка и сравнение данных
# print(value1 > value2)
# print(value1 < value2)
# print(value1 == value2)
# print(value1 == 'Hello World!!!') #Проверка на равенство
# print(value1 != 'Hello World!!!') #проверка на неравенство
# print("hello" > "hello world!!!")

#Пользователь вводит с клавиатуры три числа.
# Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.
value_number = int(input("Введите число 1: "))
value_number2 = int(input("Введите число 2: "))
value_number3 = int(input("Введите число 3: "))
сумма = value_number + value_number2 + value_number3
произведение = value_number * value_number2 * value_number3
print(f" Сумма: {сумма}")
print(f"Произведние: {произведение}")
#Задание 2
#Пользователь вводит с клавиатуры три числа.
# Первое число — зарплата за месяц,
# второе число — сумма месячного платежа по кредиту в банке,
# третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму,
# которая останется у пользователя после всех выплат.
value_number = int(input("Введите зарплату: "))
value_number2 = int(input("Введите платеж по кредиту: "))
value_number3 = int(input("Введите комуналка: "))
result = value_number - value_number2 - value_number3
print(f" ЗП: {value_number}, " 
      f" \n Платеж: {value_number2},"
      f" \n Комуналка: {value_number3},"
      f"\n Остаток: {result}")
#Экранирование символов
#Вызов спец. символа \ для создание комманды вставки символов.
# \\ - добавляет обратный слеш
# \" - добавляет двойные кавычки
# \' - добавляет одиночные кавычки
# \n - переход на новую строку
# \t - вставка 3х пробелов
# \b - удаление пред. символа
string = "Фраза для работы со строкой"
print(value_number, string, value_number2, value_number3, sep="*\n")
#sep - это строка, для вставки, между значениями элементов вывода для print
#end - вставка символа в конце строки, вместо \n
print(value_number, string, value_number2, value_number3, end="***")
#Выведите на экран надпись To be or not to be на разных строках. Пример вывода:
#To be
#            or not
#                        to be
print("To be \n \t\t or not \n \t\t\t\t to be")
print("To be","or not","to be",start='\t', end='', sep='\n')
print("To be","\n","or not","\n","to be")
#Пользователь вводит с клавиатуры три цифры.
# Необходимо создать число, содержащее эти цифры.
# Например, если с клавиатуры введено 1, 5, 7,
# тогда нужно сформировать число 157.
#a = int(input())
#b = int(input())
#c = int(input())
#print(a*100+b*10+c)
#print(str(a)+str(b)+str(c))
#print(str(a)+str(b)+str(c), sep='')
#Пользователь вводит с клавиатуры число, состоящее из четырех цифр.
# Требуется найти произведение цифр.
#Например, если с клавиатуры введено 1324,
# тогда результат произведения 1*3*2*4 = 24.
#a = int(input())
#print( (a//1000)*((a//100)%10)*((a//10)%10)*(a % 10))
#a = input()
#print(int(a[0])*int(a[1])*int(a[2])*int(a[3]))
#Строки и их свойства
string = "my Name is AaA"
print(type(string)) #Проверка типа данных
print(string + string) #Сложение строк
print(string * 4) #Умножение строк
print(string.capitalize()) #Приводит первую букву в верхний регистр
print(string.lower()) #Приводит все символы в нижний регистр
print(string.swapcase())#Меняет текущий регистр буквы на противоположный
print(string.title())#Преобразует первые буквы всех слов в верхний регистр
print(string.upper())#Преобразует все буквы в верхний регистр
print(string.count("my",start=0, end=5))#Подсчитывает кол-во элементов в строке
print(string.endswith("!"))#Проверяет, заканчивается ли строка подстрокой
print(string.startswith("!"))#Проверяет, начинается ли строка подстрокой
print(string.find("is")) #ищет подстроку в строке слево на право
print(string.rfind("AaA")) #ищет подстроку в строке право на слево
#Возвращает первое вхождение(индекс) подстроки
print(string.index("AaA")) #ищет подстроку в строке слево на право
print(string.rindex("AaA")) #ищет подстроку в строке право на слево
#Возвращает первое вхождение(индекс) подстроки, если элемента нет, будет ошибка
#Классификация(определение) строк
print(string.isalnum())#определяет, состоит ли строка из букв и чисел
print(string.isalpha())#состоит ли строка из букв
print(string.isdigit())#состоит ли строка из чисел
print(string.islower())
print(string.isupper())
print(string.istitle())
print(string.isspace()) #Проверяет наличие в строке пробельных символов
#Форматирование и выравнивание строк
print("main".center(10,"*"))#выравнивание строки по центру
print("main\t\t\tmain".expandtabs(tabsize=1))#заменяет табуляцию на пробелы
print("main main".ljust(10,"@"))#Выравнивание по левому краю
print("main main".rjust(10, "?"))#Выравнивание по правому краю
print("main main".lstrip()) #все пробельные символы слевого края будут удалены
print("main main".rstrip()) #все пробельные символы правого края будут удалены
print("main main".replace("main","own")) #заменяет подстроку\



